from typing import List
from ..models.question_model import QuestionModel
from ..models.system_parameter_model import SystemParameterModel
from .base_dto import BaseDto


class AnswerDetailDto(BaseDto):
    def __init__(self, answer_detail):
        self.question_id = answer_detail.question_id
        self.level = answer_detail.level
        self.selected_mixed_number = answer_detail.selected_mixed_number
        self.selected_numerator = answer_detail.selected_numerator
        self.selected_denominator = answer_detail.selected_denominator
        self.selected_operator = answer_detail.selected_operator
        self.answer_mixed_number = answer_detail.question.answer_mixed_number
        self.answer_numerator = answer_detail.question.answer_numerator
        self.answer_denominator = answer_detail.question.answer_denominator
        self.answer_operator = answer_detail.question.operator
        self.first_mixed_number = answer_detail.question.first_mixed_number
        self.first_numerator = answer_detail.question.first_numerator
        self.first_denominator = answer_detail.question.first_denominator
        self.second_mixed_number = answer_detail.question.second_mixed_number
        self.second_numerator = answer_detail.question.second_numerator
        self.second_denominator = answer_detail.question.second_denominator
        self.options = answer_detail.question.options
