from ..daos.class_dao import ClassDao
from ..dtos.class_dto import ClassDto


class ClassService():
    def __init__(self) -> None:
        self.class_dao = ClassDao()

    def get_classes(self, name=None):
        classes = self.class_dao.get_classes(name)
        result = [ClassDto(class_instance).serialize() for class_instance in classes]
        return result

    def insert_class(self, name):
        class_instance = self.class_dao.insert_class(name)
        return class_instance.serialize()

    def update_class(self, id, name):
        class_instance = self.class_dao.update_class(id, name)
        return class_instance.serialize()

    def delete_class(self, id):
        return self.class_dao.delete_class(id)