import os
import requests
from langchain.llms.base import LLM
from typing import Optional, List, Dict, Mapping, Any
from user import User


class Chat(LLM):
    
    url = ''
    
    @property
    def _llm_type(self) -> str:
        return "Chat"

    def _construct_query(self, prompt: str, **kwargs) -> Dict:
        """构造请求体
        """
        query_info = dict()
        query_info['human_input'] = prompt
        query_info['token'] = User().token
        if kwargs is not None and 'task' in kwargs:
            query_info['task'] = kwargs['task']
        else:
            query_info['task'] = ''
        if 'role' in kwargs:
            query_info['role'] = kwargs.get('role', None)
        if 'history' in kwargs:
            query_info['history'] = kwargs.get('history', None)
        return query_info

    @classmethod
    def _post(cls, url: str,
              query: Dict) -> Any:
        """POST请求
        """
        _headers = {"Content_Type": "application/json"}
        with requests.session() as sess:
            resp = sess.post(url,
                             json=query,
                             headers=_headers,
                             timeout=60)
        return resp

    def _call(self, prompt: str,
              stop: Optional[List[str]] = None, **kwargs) -> str:
        # construct query
        query = self._construct_query(prompt=prompt, **kwargs)
        route = '/robot'
        if 'port' not in kwargs:
            return f'请求失败: 端口不正确'
        url = f"http://{kwargs.get('host', '127.0.0.1')}:{kwargs['port']}{kwargs.get('route', '/robot')}"
        self.url = url
        try:
            resp = self._post(url=self.url, query=query)
            if resp.status_code == 200:
                resp_json = resp.json()
                if resp_json['code'] == 200:
                    res = resp_json['data']
                else:
                    res = resp_json['msg']
                return res
            else:
                return f'请求失败:\n{self.url}'
        except Exception as e:
            return f'请求失败:{e}\n{self.url}'

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters.
        """
        _param_dict = {
            "url": self.url,
        }
        return _param_dict
