from .base_dto import BaseDto
from ..models.user_model import UserModel


class UserDetailDto(BaseDto):
    def __init__(self, user: UserModel):
        self.id = user.id
        self.name = user.name
        self.account = user.account
        self.class_ = {
            'id': user.class_instance.id,
            'name': user.class_instance.name,
        }
