from typing import List
from ..models.question_model import QuestionModel
from ..models.system_parameter_model import SystemParameterModel
from .base_dto import BaseDto


class LevelDto(BaseDto):
    def __init__(self, questions: List[QuestionModel], quantity_limit: SystemParameterModel, time_limit: SystemParameterModel):
        self.questions = questions
        self.quantity_limit = int(quantity_limit.value)
        self.time_limit = int(time_limit.value)
