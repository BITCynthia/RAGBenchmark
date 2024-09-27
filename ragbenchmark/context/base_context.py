from typing import Dict
from abc import ABC, abstractmethod

class BaseContext(ABC):
    def __init__(self) -> None:
        self._text: str = ""

    @abstractmethod
    def _extract(self, context_dict: Dict) -> None:
        pass

    @property
    def text(self) -> str:
        return self._text