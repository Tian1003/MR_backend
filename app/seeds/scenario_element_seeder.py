from app.models.scenario_element_model import ScenarioElementModel
from flask_seeder import Seeder
from app.database import db  # ✅ 確保導入 db

class ScenarioElementSeeder(Seeder):
    def run(self):
        scenario_element1 = ScenarioElementModel(
            scenario_id=1,
            name="瑪格麗特披薩",
            level=1,
        )
        db.session.add(scenario_element1)  # ✅ 直接使用 db.session
        scenario_element2 = ScenarioElementModel(
            scenario_id=1,
            name="臘腸披薩",
            level=2,
        )
        db.session.add(scenario_element2)
        scenario_element3 = ScenarioElementModel(
            scenario_id=1,
            name="燻雞披薩",
            level=3,
        )
        db.session.add(scenario_element3)
        db.session.commit()  # ✅ 確保提交資料
        print("scenario elements added")
