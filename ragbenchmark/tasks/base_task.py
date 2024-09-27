from typing import List, Dict

class BaseTask:
    def __init__(self) -> None:
        self.id: str
        self.question: str
        self.answer: str
        self.contexts: List[Dict]