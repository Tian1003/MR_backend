from ..models.scenario_question_model import ScenarioQuestionModel
from ..models.scenario_element_model import ScenarioElementModel
from sqlalchemy.sql import func


class ScenarioQuestionDao():
    def get_random_questions(self, scenario_id, level):
        columns = [
            ScenarioQuestionModel.id,
            ScenarioQuestionModel.scenario_element_id,
            ScenarioQuestionModel.mixed_number,
            ScenarioQuestionModel.numerator,
            ScenarioQuestionModel.denominator,
            ScenarioElementModel.name.label("scenario_element_name"),
        ]

        all_questions = []
        
        for i in range(1, level + 1):
            query = (
                ScenarioQuestionModel.query
                .with_entities(*columns)
                .join(ScenarioElementModel, ScenarioQuestionModel.scenario_element_id == ScenarioElementModel.id)
                .filter(ScenarioElementModel.scenario_id == scenario_id)
                .filter(ScenarioElementModel.level == i)
                .order_by(func.random())
                .limit(1)
            )

            question = query.first()
            if question:
                all_questions.append(question)

        total = len(all_questions)
        return all_questions, total
