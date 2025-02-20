import random
from sqlalchemy.sql import func
from .base_seeder import BaseSeeder
from app.models.answer_detail_model import AnswerDetailModel
from app.models.question_model import QuestionModel
from app.database import db


class AnswerDetailSeeder(BaseSeeder):
    def run(self):
        question_types = ["quantity_limited_practices", "quantity_limited_tests",
                          "time_limited_practices", "time_limited_tests"]

        all_questions = QuestionModel.query.all()
        question_ids = [question.id for question in all_questions]

        for _ in range(1, 1001):
            type_id = random.randint(1, 4)
            question_type = random.choice(question_types)

            for level in range(1, 4):
                question_id = random.choice(question_ids)
                question = QuestionModel.query.filter(QuestionModel.id == question_id).first()

                if question:
                    option = random.choice(question.options)
                    selected_mixed_number = option["mixed_number"]
                    selected_numerator = option["numerator"]
                    selected_denominator = option["denominator"]
                    selected_operator = random.choice([">", "<", "="])

                    answer_detail = AnswerDetailModel(
                        record_id=_,
                        question_id=question.id,
                        question_type=question_type,
                        level=level,
                        selected_mixed_number=selected_mixed_number,
                        selected_numerator=selected_numerator,
                        selected_denominator=selected_denominator,
                        selected_operator=selected_operator
                    )

                    db.session.add(answer_detail)

            db.session.commit()
        print("answer_detail added")
