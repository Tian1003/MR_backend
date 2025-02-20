import os
import random
from dotenv import load_dotenv

from app.generators.timestamp_generator import TimestampGenerator
from app.models.scenario_practice_model import ScenarioPracticeModel
from app.models.user_model import UserModel
from .base_seeder import BaseSeeder


class ScenarioPracticeSeeder(BaseSeeder):
    def run(self):
        load_dotenv()
        if (os.getenv('ENV') == 'develop'):
            for _ in range(1000):
                quantity_limited_practice = ScenarioPracticeModel(
                    user_id=self.get_model_random_id(UserModel),
                    scenario_id=1,
                    level1_time=random.randint(10, 100),
                    level2_time=random.randint(10, 100),
                    level3_time=random.randint(10, 100),
                    finished_at=TimestampGenerator().generate()
                )
                self.db.session.add(quantity_limited_practice)

            self.db.session.commit()
            print("scenario_practices added")
