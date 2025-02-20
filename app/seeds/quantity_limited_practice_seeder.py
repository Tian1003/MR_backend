import os
import random
from dotenv import load_dotenv

from app.generators.timestamp_generator import TimestampGenerator
from app.models.quantity_limited_practice_model import QuantityLimitedPracticeModel
from app.models.user_model import UserModel
from app.models.type_model import TypeModel
from .base_seeder import BaseSeeder


class QuantityLimitedPracticeSeeder(BaseSeeder):
    def run(self):
        load_dotenv()
        if (os.getenv('ENV') == 'develop'):
            level1_total_quantity = self.get_system_parameter(
                "level_1_quantity_limit").value
            level2_total_quantity = self.get_system_parameter(
                "level_2_quantity_limit").value
            level3_total_quantity = self.get_system_parameter(
                "level_3_quantity_limit").value

            for _ in range(1000):
                quantity_limited_practice = QuantityLimitedPracticeModel(
                    user_id=self.get_model_random_id(UserModel, [1, 2]),
                    type_id=self.get_model_random_id(TypeModel),
                    level1_total_quantity=level1_total_quantity,
                    level1_time=random.randint(10, 100),
                    level2_total_quantity=level2_total_quantity,
                    level2_time=random.randint(10, 100),
                    level3_total_quantity=level3_total_quantity,
                    level3_time=random.randint(10, 100),
                    finished_at=TimestampGenerator().generate()
                )
                self.db.session.add(quantity_limited_practice)

            self.db.session.commit()
            print("quantity_limited_practices added")
