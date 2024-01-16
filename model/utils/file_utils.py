import yaml


# 读取yaml文件
def read_configer(file):
    with open(file, mode='r', encoding='utf-8') as f:
        res = yaml.safe_load(f)
        return res

# 写入yaml文件
def write_configer(file, data):
    with open(file, mode="w", encoding='utf-8') as f:
        yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
