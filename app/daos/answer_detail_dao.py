from sqlalchemy import and_
from app.database import db
from ..models.answer_detail_model import AnswerDetailModel
from ..models.question_model import QuestionModel


class AnswerDetailDao():
    def get_answer_detail(self, record_id, question_type, level):
        result = (
            AnswerDetailModel.query
            .join(QuestionModel)
            .filter(and_(AnswerDetailModel.record_id == record_id,
                         AnswerDetailModel.question_type == question_type,
                         AnswerDetailModel.level == level)).all())

        return result, len(result)

    def insert_answer_detail(self, record_id, question_id, question_type, level, selected_mixed_number, selected_numerator, selected_denominator, selected_operator):
        answer_detail = AnswerDetailModel(
            record_id=record_id,
            question_id=question_id,
            question_type=question_type,
            level=level,
            selected_mixed_number=selected_mixed_number,
            selected_numerator=selected_numerator,
            selected_denominator=selected_denominator,
            selected_operator=selected_operator,
        )

        db.session.add(answer_detail)
        db.session.commit()
