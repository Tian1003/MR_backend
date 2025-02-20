from ..dtos.base_dto import BaseDto


class RankDto(BaseDto):
    def __init__(self, model):
        self.id = model.id
        self.user = {
            "id": model.user.id,
            "name": model.user.name,
        }
        self.class_ = {
            "id": model.user.class_instance.id,
            "name": model.user.class_instance.name,
        }
        self.type = {
            "id": model.type.id,
            "name": model.type.name,
        }
        self.level_time = model.level1_time + model.level2_time + model.level3_time
        self.correct_quantity = (
            (getattr(model, 'level1_correct_quantity', 0) or 0) +
            (getattr(model, 'level2_correct_quantity', 0) or 0) +
            (getattr(model, 'level3_correct_quantity', 0) or 0)
        )
