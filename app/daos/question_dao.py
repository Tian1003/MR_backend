from ..models.question_model import QuestionModel
from sqlalchemy.sql import func


class QuestionDao():
    def get_random_questions(self, type_id, level, quantity_limit):
        columns = [
            QuestionModel.id,
            QuestionModel.first_mixed_number,
            QuestionModel.first_numerator,
            QuestionModel.first_denominator,
        ]

        if level == 1:
            columns += [
                QuestionModel.options,
            ]

        if level >= 2:
            columns += [
                QuestionModel.second_mixed_number,
                QuestionModel.second_numerator,
                QuestionModel.second_denominator,
            ]

        if level == 3:
            columns += [
                QuestionModel.options,
                QuestionModel.operator,
                QuestionModel.answer_mixed_number,
                QuestionModel.answer_numerator,
                QuestionModel.answer_denominator,
            ]

        query = (
            QuestionModel.query
            .with_entities(*columns)
            .filter(QuestionModel.type_id == type_id)
            .distinct()
            .order_by(func.random())
            .limit(quantity_limit)
        )

        questions = query.all()
        total = query.count()
        return questions, total
