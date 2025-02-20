from ..dtos.base_dto import BaseDto
from ..models.scenario_practice_model import ScenarioPracticeModel


class ScenarioPracticeDto(BaseDto):
    def __init__(self, model: ScenarioPracticeModel):
        self.id = model.id
        self.user = {
            "id": model.user.id,
            "name": model.user.name,
        }
        self.class_ = {
            "id": model.user.class_instance.id,
            "name": model.user.class_instance.name,
        }
        self.scenario = {
            "id": model.scenario.id,
            "name": model.scenario.name,
        }
        self.level1_time = model.level1_time
        self.level2_time = model.level2_time
        self.level3_time = model.level3_time
        self.finished_at = model.finished_at
