from typing import List


class BaseDataset:
    def __init__(self, dataset_name: str, documents: List[str]):
        self.dataset_name = dataset_name
        self.documents = documents
        self.tasks