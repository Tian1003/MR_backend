from ..dtos.level_dto import LevelDto
from ..daos.question_dao import QuestionDao
from ..daos.system_parameter_dao import SystemParameterDao


class LevelService():
    def __init__(self) -> None:
        self.question_dao = QuestionDao()
        self.system_parameter_dao = SystemParameterDao()

    def _transform_level2_data(self, type_id, questions):
        if type_id == 3:
            for question in questions:
                first_processed_numerator = question["first_mixed_number"] * question["first_denominator"] + question["first_numerator"]
                second_processed_numerator = question["second_mixed_number"] * question["second_denominator"] + question["second_numerator"]
                question["operator"] = "=" if first_processed_numerator == second_processed_numerator else ">" if first_processed_numerator > second_processed_numerator else "<"
        else:
            for question in questions:
                question["operator"] = "=" if question["first_numerator"] == question[
                    "second_numerator"] else ">" if question["first_numerator"] > question["second_numerator"] else "<"
        return questions

    def get_level_data(self, type_id, level):
        time_limit = self.system_parameter_dao.get_time_limit(level=level)
        quantity_limit = self.system_parameter_dao.get_quantity_limit(
            level=level)

        questions, total = self.question_dao.get_random_questions(
            type_id=type_id,
            level=level,
            quantity_limit=quantity_limit.value
        )
        question_list = [question._asdict() for question in questions]

        question_list = self._transform_level2_data(type_id, 
            question_list) if level == 2 else question_list
        result = LevelDto(question_list, quantity_limit, time_limit)

        return result.serialize(), total
