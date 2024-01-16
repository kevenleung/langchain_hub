from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from llm.chatglm3.llm_chatglm3 import ChatGLM3


def handle_demo_task(query, uid):
    llm = ChatGLM3()
    intention = ['企业查询', '政策查询', '通用', '其他']

    template = """以下用三个反引号分隔的问题的分类文本是什么？
    并且侧重在['企业查询', '政策查询']上。
    用一个单词回答：「企业查询」或「政策查询。
    如果都不是，请回答：「其他」。
    如果不知道，请回答：「通用」。
    你只能回答以上限定的单词，不能自己创造。
    分类文本: ```{question}```"""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    cnt = 0
    while True:
        cnt += 1
        question = query
        if question.strip() == "stop":
            break
        response = llm_chain.invoke(question)
        response['text'].replace('「', '').replace('」','')
        print("\nChatGLM：", response['text'])
        if response['text'] not in intention:
            for i in range(10):
                response = llm_chain.invoke(question)
                print(f"\n第{i+1}次， ChatGLM：", response['text'])
                if response['text'].replace('「', '').replace('」','').replace('。','')  in intention:
                    break
        if cnt > 10:
            break
    print('')
    return {}