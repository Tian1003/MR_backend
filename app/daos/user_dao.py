from app.database import db
from ..models.user_model import UserModel
from ..models.class_model import ClassModel


class UserDao():
    def get_users(self, name=None, account=None, class_id_list=None):
        query = (
            UserModel.query.filter(
                UserModel.account.notin_(["teacher", "developer"])
            )
            .join(ClassModel)
        )

        if name is not None:
            query = query.filter(UserModel.name.like(f'%{name}%'))

        if account is not None:
            query = query.filter(UserModel.account.like(f'%{account}%'))

        if class_id_list is not None:
            class_id_list = [int(class_id) for class_id in class_id_list.split(',') if class_id]
            query = query.filter(ClassModel.id.in_(class_id_list))

        users = query.order_by(UserModel.id).all()
        total = query.count()
        return users, total

    def get_user(self, id):
        result = UserModel.query.get(id)
        return result

    def insert_user(self, class_id, name, account):
        print("class_id, name, account", class_id, name, account)
        user = UserModel(
            class_id=class_id,
            name=name,
            account=account,
        )

        db.session.add(user)
        db.session.commit()

        new_user = UserModel.query.get(user.id)

        return new_user

    def update_user(self, id, class_id, account, name):
        user = UserModel.query.get(id)

        setattr(user, 'class_id', class_id)
        setattr(user, 'account', account)
        setattr(user, 'name', name)
        db.session.commit()

        new_user = UserModel.query.get(id)
        return new_user

    def delete_user(self, id):
        user = UserModel.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return None
