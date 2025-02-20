from sqlalchemy.sql import func
from app.database import db


class ModelGenerator():
    def __init__(self, model: db.Model):
        self.model = model

    def generate(self):
        model_instance = self.model.query.order_by(func.random()).first()
        return model_instance.id
