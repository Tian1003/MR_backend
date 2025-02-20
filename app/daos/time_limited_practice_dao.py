from datetime import datetime
from app.database import db
from sqlalchemy.orm import joinedload
from ..models.time_limited_practice_model import TimeLimitedPracticeModel
from ..models.user_model import UserModel
from ..models.type_model import TypeModel
from ..models.class_model import ClassModel


class TimeLimitedPracticeDao():
    def get_all_time_limited_practices(self, user_id=None):
        query = (
            TimeLimitedPracticeModel.query
            .join(UserModel)
            .join(TypeModel)
            .join(ClassModel)
            .order_by(
                TimeLimitedPracticeModel.finished_at.desc())
        )

        if user_id is not None:
            query = query.filter(UserModel.id == user_id)

        return query.all(), query.count()

    def get_time_limited_practices(self, name=None, class_id_list=None, type_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        query = (
            TimeLimitedPracticeModel.query
            .join(UserModel)
            .join(TypeModel)
            .join(ClassModel)
            .order_by(
                TimeLimitedPracticeModel.finished_at.desc())
        )

        if name is not None:
            query = query.filter(UserModel.name.ilike(f"%{name}%"))

        if class_id_list is not None:
            class_id_list = [int(class_id)
                             for class_id in class_id_list.split(',') if class_id]
            query = query.filter(ClassModel.id.in_(class_id_list))

        if type_id_list is not None:
            type_id_list = [int(type_id)
                            for type_id in type_id_list.split(',') if type_id]
            query = query.filter(TypeModel.id.in_(type_id_list))

        if finished_start is not None and finished_end is not None:
            query = query.filter(
                TimeLimitedPracticeModel.finished_at.between(finished_start, finished_end))

        time_limited_practices = query.paginate(
            page=page, per_page=per_page, count=True)
        from_index = (time_limited_practices.page - 1) * per_page + 1
        to_index = min(from_index + per_page - 1,
                       time_limited_practices.total)

        return time_limited_practices.items, time_limited_practices.pages, time_limited_practices.total, from_index, to_index

    def get_time_limited_practices_chart_data(self, user_id, finished_start=None, finished_end=None):
        query = (
            TimeLimitedPracticeModel.query
            .filter(TimeLimitedPracticeModel.user_id == user_id)
            .order_by(
                TimeLimitedPracticeModel.finished_at.desc())
        )

        if finished_start is not None and finished_end is not None:
            query = query.filter(
                TimeLimitedPracticeModel.finished_at.between(
                    finished_start, finished_end)
            )
        else:
            query = query.limit(5)

        result = query.all()

        return result

    def insert_time_limited_practice(self, user_id, type_id, total_quantity, correct_quantity, time, time_limit):
        time_limited_practice = TimeLimitedPracticeModel(
            user_id=user_id,
            type_id=type_id,
            level1_total_quantity=total_quantity,
            level1_correct_quantity=correct_quantity,
            level1_time=time,
            level1_time_limit=time_limit,
            finished_at=datetime.now()
        )

        db.session.add(time_limited_practice)
        db.session.commit()

        new_time_limited_practice = TimeLimitedPracticeModel.query.get(
            time_limited_practice.id)

        return new_time_limited_practice

    def update_time_limited_practice(self, id, level, total_quantity, correct_quantity, time, time_limit):
        time_limited_practice = TimeLimitedPracticeModel.query.get(id)

        setattr(time_limited_practice,
                f'level{level}_total_quantity', total_quantity)
        setattr(time_limited_practice,
                f'level{level}_correct_quantity', correct_quantity)
        setattr(time_limited_practice, f'level{level}_time', time)
        setattr(time_limited_practice,
                f'level{level}_time_limit', time_limit)
        setattr(time_limited_practice, 'finished_at', datetime.now())

        db.session.commit()

        new_time_limited_practice = TimeLimitedPracticeModel.query.get(
            id)
        return new_time_limited_practice
