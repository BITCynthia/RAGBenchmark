import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .base_context import BaseContext

class PubMedContext(BaseContext):
    def __init__(self) -> None:
        super().__init__()