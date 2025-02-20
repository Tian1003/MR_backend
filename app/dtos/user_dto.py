from .base_dto import BaseDto
from ..models.user_model import UserModel


class UserDto(BaseDto):
    def __init__(self, user: UserModel):
        self.id = user.id
        self.name = user.name
        self.account = user.account
