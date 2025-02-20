from ..dtos.base_dto import BaseDto


class RecordDto(BaseDto):
    def __init__(self, model):
        self.id = model.id
        self.user_id = model.user_id
