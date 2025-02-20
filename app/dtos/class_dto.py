from .base_dto import BaseDto
from .user_dto import UserDto
from ..models.class_model import ClassModel


class ClassDto(BaseDto):
    def __init__(self, class_instance: ClassModel):
        self.id = class_instance.id
        self.name = class_instance.name
        self.users = [UserDto(user).serialize() for user in class_instance.users
                      if user.account not in ["teacher", "developer"]]
