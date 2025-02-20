from ..dtos.base_dto import BaseDto
from ..models.quantity_limited_test_model import QuantityLimitedTestModel


class QuantityLimitedTestDto(BaseDto):
    def __init__(self, model: QuantityLimitedTestModel):
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

        self.level1_correct_quantity = model.level1_correct_quantity
        self.level1_incorrect_quantity = ((model.level1_total_quantity or 0) - (model.level1_correct_quantity or 0))
        self.level1_total_quantity = model.level1_total_quantity
        self.level1_time = model.level1_time
        self.level2_correct_quantity = model.level2_correct_quantity
        self.level2_incorrect_quantity = ((model.level2_total_quantity or 0) - (model.level2_correct_quantity or 0))
        self.level2_total_quantity = model.level2_total_quantity
        self.level2_time = model.level2_time
        self.level3_correct_quantity = model.level3_correct_quantity
        self.level3_incorrect_quantity = ((model.level3_total_quantity or 0) - (model.level3_correct_quantity or 0))
        self.level3_total_quantity = model.level3_total_quantity
        self.level3_time = model.level3_time
        self.finished_at = model.finished_at
