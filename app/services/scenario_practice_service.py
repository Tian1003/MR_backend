from ..daos.scenario_practice_dao import ScenarioPracticeDao
from ..dtos.record_dto import RecordDto
from ..dtos.scenario_practice_dto import ScenarioPracticeDto


class ScenarioPracticeService():
    def __init__(self) -> None:
        self.scenario_practice_dao = ScenarioPracticeDao()

    def get_all_scenario_practices(self):
        scenario_practices, total = self.scenario_practice_dao.get_all_scenario_practices()
        print(scenario_practices[0].__dict__)
        result = [ScenarioPracticeDto(
            model).serialize() for model in scenario_practices]

        return result, total

    def get_scenario_practices(self, name=None, class_id_list=None, scenario_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        scenario_practices, max_page, total, from_index, to_index = self.scenario_practice_dao.get_scenario_practices(
            name, class_id_list, scenario_id_list, finished_start, finished_end, page, per_page)
        result = [ScenarioPracticeDto(
            model).serialize() for model in scenario_practices]

        return result, max_page, total, from_index, to_index

    def get_scenario_practices_chart_data(self, user_id, finished_start=None, finished_end=None):
        level1_times = []
        level1_finished_at_list = []

        level2_times = []
        level2_finished_at_list = []

        level3_times = []
        level3_finished_at_list = []

        scenario_practices = self.scenario_practice_dao.get_scenario_practices_chart_data(
            user_id, finished_start, finished_end)

        for model in scenario_practices:
            level1_times.append(model.level1_time)
            level1_finished_at_list.append(model.finished_at)

            level2_times.append(model.level2_time)
            level2_finished_at_list.append(model.finished_at)

            level3_times.append(model.level3_time)
            level3_finished_at_list.append(model.finished_at)

        result = {
            "level1_times": level1_times,
            "level1_finished_at_list": level1_finished_at_list,

            "level2_times": level2_times,
            "level2_finished_at_list": level2_finished_at_list,

            "level3_times": level3_times,
            "level3_finished_at_list": level3_finished_at_list,
        }

        return result

    def insert_scenario_practice(self, user_id, scenario_id, level1_time, level2_time, level3_time):
        result = self.scenario_practice_dao.insert_scenario_practice(
            user_id=user_id,
            scenario_id=scenario_id,
            level1_time=level1_time,
            level2_time=level2_time,
            level3_time=level3_time,
        )

        return RecordDto(result).serialize()
