from app.models.scenario_element_model import ScenarioElementModel
from flask_seeder import Seeder

class ScenarioElementSeeder(Seeder):
    def run(self):
        scenario_element1 = ScenarioElementModel(
            scenario_id=1,
            name="瑪格麗特披薩",
            level=1,
        )
        self.db.session.add(scenario_element1)
        scenario_element2 = ScenarioElementModel(
            scenario_id=1,
            name="臘腸披薩",
            level=2,
        )
        self.db.session.add(scenario_element2)
        scenario_element3 = ScenarioElementModel(
            scenario_id=1,
            name="燻雞披薩",
            level=3,
        )
        self.db.session.add(scenario_element3)
        self.db.session.commit()
        print("scenario elements added")
