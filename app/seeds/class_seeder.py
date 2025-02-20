from .base_seeder import BaseSeeder
from app.models.class_model import ClassModel


class ClassSeeder(BaseSeeder):
    def run(self):
        for i in range(6):
            class_ = ClassModel(
                name=f"班級{i+1}"
            )
            self.db.session.add(class_)
        self.db.session.commit()
        print("classes added")
