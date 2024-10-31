import os
import sys
from typing import Optional, Dict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chat_models.base_chat_model import BaseChatModel
from tasks.base_task import BaseTask
class TaskEvaluator:
    def __init__(self, task: BaseTask, chat_model: Optional[BaseChatModel]):
        self.task = task
        self.chat_model = chat_model
        # metrics by page number
        self.recall_by_page_number: Dict[str, float] = None
        self.precision_by_page_number: Dict[str, float] = None