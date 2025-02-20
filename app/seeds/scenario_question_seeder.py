from .base_seeder import BaseSeeder
from app.models.scenario_question_model import ScenarioQuestionModel


class ScenarioQuestionSeeder(BaseSeeder):
    def run(self):
        denominators = [4, 6, 8, 12]
        # should get current scenario element amount
        for scenario_element_id in range(1, 4):
            for denominator in denominators:
                scenario_question = ScenarioQuestionModel(
                        scenario_element_id=scenario_element_id,
                        mixed_number=1,
                        numerator=None,
                        denominator=None
                    )
                self.db.session.add(scenario_question)
                for numerator in range(1, denominator):
                    scenario_question = ScenarioQuestionModel(
                        scenario_element_id=scenario_element_id,
                        mixed_number=None,
                        numerator=numerator,
                        denominator=denominator
                    )
                    self.db.session.add(scenario_question)
        self.db.session.commit()
        print("scenario questions added")
