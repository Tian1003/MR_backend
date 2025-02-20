from ..daos.answer_detail_dao import AnswerDetailDao
from ..dtos.answer_detail_dto import AnswerDetailDto

class AnswerDetailService():
    def __init__(self) -> None:
        self.answer_detail_dao = AnswerDetailDao()

    def get_answer_detail(self, record_id, question_type, level):
        answer_detail_with_question_list, total = self.answer_detail_dao.get_answer_detail(
            record_id, question_type, level)
        result = [AnswerDetailDto(model).serialize() for model in answer_detail_with_question_list]

        if level == 2:
            for answer_detail in result:
                answer_detail["answer_operator"] = "=" if answer_detail["first_numerator"] == answer_detail["second_numerator"] else ">" if answer_detail["first_numerator"] > answer_detail["second_numerator"] else "<"
        return result, total
