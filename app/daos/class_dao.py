from sqlalchemy.orm import joinedload
from app.database import db
from ..models.class_model import ClassModel
from ..models.user_model import UserModel


class ClassDao():
    def get_classes(self, name=None):
        query = (
            ClassModel.query
            .outerjoin(UserModel)
        )

        if name is not None:
            query = query.filter(ClassModel.name.like(f'%{name}%'))

        classes = query.order_by(ClassModel.id).all()
        return classes

    def insert_class(self, name):
        class_model = ClassModel(name=name)

        db.session.add(class_model)
        db.session.commit()

        new_class_model = ClassModel.query.get(class_model.id)
        return new_class_model

    def update_class(self, id, name):
        class_model = ClassModel.query.get(id)

        setattr(class_model, 'name', name)
        db.session.commit()

        new_class_model = ClassModel.query.get(id)
        return new_class_model

    def delete_class(self, id):
        class_model = ClassModel.query.get(id)

        db.session.delete(class_model)
        db.session.commit()
        return None
