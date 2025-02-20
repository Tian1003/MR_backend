from ..daos.scenario_question_dao import ScenarioQuestionDao


class ScenarioLevelService():
    def __init__(self) -> None:
        self.scenario_question_dao = ScenarioQuestionDao()

    def get_scenario_level_data(self, scenario_id, level):

        questions, total = self.scenario_question_dao.get_random_questions(
            scenario_id=scenario_id,
            level=level,
        )
        
        question_list = [question._asdict() for question in questions]
        return question_list, total
