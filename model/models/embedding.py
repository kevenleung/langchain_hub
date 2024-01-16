
from utils.singleton import singleton_embedding
from sentence_transformers import SentenceTransformer


@singleton_embedding
class Embbeding:
    def __init__(self, path):
        super().__init__()
        self.path = path
        self._load_model(self.path)

    def _load_model(self, model_name_or_path=None):
        if model_name_or_path is not None and model_name_or_path != '':
                self.model = SentenceTransformer(model_name_or_path, device="cuda")
        else:
            self.model = None
            
    