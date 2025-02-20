from faker import Faker
from sqlalchemy.sql import func
from app.database import db
from app.models.system_parameter_model import SystemParameterModel
from app.models.base_model import BaseModel


class BaseSeeder():
    def __init__(self):
        self.db = db
        self.faker = Faker('zh_TW')

    def get_model_random_id(self, model: BaseModel, exclude_ids=None):
        query = model.query
        if exclude_ids:
            query = query.filter(~model.id.in_(exclude_ids))
        model_instance = query.order_by(func.random()).first()
        return model_instance.id if model_instance else None


    def get_system_parameter(self, key):
        return SystemParameterModel.query.filter_by(key=key).first()
