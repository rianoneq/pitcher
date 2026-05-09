import pickle
from pathlib import Path

from entity.peaks import PeaksParams


class CacheService:
    def __init__(self, params: PeaksParams):
        self.params = params

    def load(self):
        with open(self.params.cache_path, 'rb') as f:
            return pickle.load(f)

    def exists(self) -> bool:
        print(Path(self.params.cache_path), self.params.cache_path)
        return Path(self.params.cache_path).exists()

    def save(self, data):
        with open(self.params.cache_path, 'wb') as f:
            pickle.dump(data, f)
