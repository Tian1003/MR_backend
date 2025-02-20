from app.database import db
from app.models.type_model import TypeModel


class TypeSeeder():
    def run(self):
        types = ["真分數", "假分數", "帶分數"]

        for name in types:
            type_model = TypeModel(name=name)
            db.session.add(type_model)

        print("types added")
