from app.database import db
from app.models.system_parameter_model import SystemParameterModel


class SystemParameterSeeder():
    def run(self):
        parameters = {
            "level_1_time_limit": 100,
            "level_1_quantity_limit": 5,
            "level_2_time_limit": 200,
            "level_2_quantity_limit": 5,
            "level_3_time_limit": 300,
            "level_3_quantity_limit": 5,
        }

        for key, value in parameters.items():
            system_parameter_model = SystemParameterModel(key=key, value=value)
            db.session.add(system_parameter_model)

        print("system parameters added")
