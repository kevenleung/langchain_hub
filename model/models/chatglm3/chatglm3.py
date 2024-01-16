
from utils.singleton import singleton_model
from transformers import AutoModel, AutoTokenizer, AutoConfig

@singleton_model
class ChatGLM3:

    def __init__(self, path):
        super().__init__()
        self.llm_path = path
        self._load_model(self.llm_path)
    
    def _load_model(self, model_name_or_path=None):
        model_config = AutoConfig.from_pretrained(model_name_or_path, trust_remote_code=True)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_name_or_path, config=model_config,
                                                trust_remote_code=True).half().cuda()
        self.model = self.model.eval()

    