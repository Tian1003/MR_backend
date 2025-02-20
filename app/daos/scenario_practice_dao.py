from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import joinedload
from app.database import db
from ..models.scenario_model import ScenarioModel
from ..models.scenario_practice_model import ScenarioPracticeModel
from ..models.user_model import UserModel
from ..models.class_model import ClassModel


class ScenarioPracticeDao():
    def get_all_scenario_practices(self):
        query = (
            ScenarioPracticeModel.query
            .join(UserModel)
            .join(ClassModel)
            .join(ScenarioModel)
            .order_by(
                ScenarioPracticeModel.finished_at.desc())
        )

        return query.all(), query.count()

    def get_scenario_practices(self, name=None, class_id_list=None, scenario_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        query = (
            ScenarioPracticeModel.query
            .join(UserModel)
            .join(ClassModel)
            .join(ScenarioModel)
            .order_by(
                ScenarioPracticeModel.finished_at.desc())
        )

        if name is not None:
            query = query.filter(UserModel.name.ilike(f"%{name}%"))

        if class_id_list is not None:
            class_id_list = [int(class_id)
                             for class_id in class_id_list.split(',') if class_id]
            query = query.filter(ClassModel.id.in_(class_id_list))

        if scenario_id_list is not None:
            scenario_id_list = [int(type_id)
                            for type_id in scenario_id_list.split(',') if type_id]
            query = query.filter(ScenarioModel.id.in_(scenario_id_list))

        if finished_start is not None and finished_end is not None:
            query = query.filter(
                ScenarioPracticeModel.finished_at.between(
                    finished_start, finished_end)
            )

        quantity_limited_practices = query.paginate(
            page=page, per_page=per_page, count=True)
        from_index = (quantity_limited_practices.page - 1) * per_page + 1
        to_index = min(from_index + per_page - 1,
                       quantity_limited_practices.total)

        return quantity_limited_practices.items, quantity_limited_practices.pages, quantity_limited_practices.total, from_index, to_index

    def get_scenario_practices_chart_data(self, user_id, finished_start=None, finished_end=None):
        query = (
            ScenarioPracticeModel.query
            .filter(ScenarioPracticeModel.user_id == user_id)
            .order_by(
                ScenarioPracticeModel.finished_at.desc())
        )

        if finished_start is not None and finished_end is not None:
            query = query.filter(
                ScenarioPracticeModel.finished_at.between(
                    finished_start, finished_end)
            )
        else:
            query = query.limit(5)

        result = query.all()

        return result

    def insert_scenario_practice(self, user_id, scenario_id, level1_time, level2_time, level3_time):
        scenario_practice = ScenarioPracticeModel(
            user_id=user_id,
            scenario_id=scenario_id,
            level1_time=level1_time,
            level2_time=level2_time,
            level3_time=level3_time,
            finished_at=datetime.now()
        )

        db.session.add(scenario_practice)
        db.session.commit()

        new_scenario_practice = ScenarioPracticeModel.query.get(
            scenario_practice.id)

        return new_scenario_practice