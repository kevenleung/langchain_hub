import os
from utils.file_utils import read_configer

llms_conf_path = f"{os.path.abspath('.')}/model/configs/model_config.yaml"


class LLMsConfig:
    def __init__(self, conf_type):
        super().__init__()
        self.llms = self._load_config(conf_type)

    def _load_config(self, key):
        datas = []
        if key == 'llms':
            conf_info = read_configer(llms_conf_path)
            llms_info = conf_info[key]
            for name in conf_info['llms_load']:
                llm_info = llms_info.get(name, None)
                if llm_info is not None:
                    model_dir = llm_info.get('model_dir', 'default')
                    if model_dir == 'default':
                        llm_info['model_dir'] = conf_info['model_base_dir']
                    llm_info['path'] = f"{llm_info['model_dir']}/{llm_info['repo_id']}"
                    datas.append(llm_info)


        return datas