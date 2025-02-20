from .base_seeder import BaseSeeder
from app.models.scenario_model import ScenarioModel


class ScenarioSeeder(BaseSeeder):
    def run(self):
        scenario = ScenarioModel(
            name="賣披薩"
        )
        self.db.session.add(scenario)
        self.db.session.commit()
        print("scenarios added")
