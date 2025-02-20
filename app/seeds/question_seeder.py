import os
import json
from app.database import db
from app.models.question_model import QuestionModel


class QuestionSeeder():
    def __init__(self, entry):
        self.entry = entry

    def run(self):
        init_data_path = os.path.join(self.entry, "init_data")
        files = os.listdir(init_data_path)

        for file_name in files:
            if file_name.endswith('.json'):
                file_path = os.path.join(init_data_path, file_name)

                with open(file_path, 'r') as file:
                    data = json.load(file)

                for question in data['questions']:
                    question_instance = QuestionModel(
                        type_id=question['type_id'],
                        first_mixed_number=question['first_mixed_number'],
                        first_numerator=question['first_numerator'],
                        first_denominator=question['first_denominator'],
                        operator=question['operator'],
                        second_mixed_number=question['second_mixed_number'],
                        second_numerator=question['second_numerator'],
                        second_denominator=question['second_denominator'],
                        answer_mixed_number=question['answer_mixed_number'],
                        answer_numerator=question['answer_numerator'],
                        answer_denominator=question['answer_denominator'],
                        options=question['options']
                    )

                    db.session.add(question_instance)
                db.session.commit()

        print("questions added")
