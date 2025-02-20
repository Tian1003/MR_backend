from ..daos.user_dao import UserDao
from ..dtos.user_detail_dto import UserDetailDto


class UserService():
    def __init__(self) -> None:
        self.user_dao = UserDao()

    def get_users(self, name=None, account=None, class_id_list=None):
        users, total = self.user_dao.get_users(name, account, class_id_list)
        result = [UserDetailDto(user).serialize() for user in users]
        return result, total

    def get_user(self, id):
        result = self.user_dao.get_user(id)
        return UserDetailDto(result).serialize()

    def insert_user(self, class_id, name, account):
        result = self.user_dao.insert_user(class_id, name, account)
        return UserDetailDto(result).serialize()

    def update_user(self, id, class_id, account, name):
        result = self.user_dao.update_user(
            id=id,
            class_id=class_id,
            account=account,
            name=name,
        )
        return UserDetailDto(result).serialize()

    def delete_user(self, id):
        return self.user_dao.delete_user(id)
