from app.database import db
from sqlalchemy.ext.declarative import DeclarativeMeta
import json


class BaseModel(db.Model):
    __abstract__ = True

    hidden_list = ["password", ]

    def serialize(self):
        serialized_data = {}
        for key, value in self.__dict__.items():
            if key in self.hidden_list:
                continue
            if not key.startswith('_') and not isinstance(value.__class__, DeclarativeMeta):
                serialized_data[key] = value
        return serialized_data
