import re
from marshmallow import Schema, ValidationError
from ..models.user_model import UserModel
from ..models.type_model import TypeModel
from ..models.class_model import ClassModel
from ..models.question_model import QuestionModel
from ..models.quantity_limited_practice_model import QuantityLimitedPracticeModel
from ..models.quantity_limited_test_model import QuantityLimitedTestModel
from ..models.time_limited_practice_model import TimeLimitedPracticeModel
from ..models.time_limited_test_model import TimeLimitedTestModel
from ..models.scenario_model import ScenarioModel


class BaseSchema(Schema):
    def user_account_exists(account):
        user = UserModel.query.filter(UserModel.account == account).first()
        if user:
            raise ValidationError('Account already exists')

    def user_account_not_exists(account):
        user = UserModel.query.filter(UserModel.account == account).first()
        if not user:
            raise ValidationError('Account not found')

    def user_name_not_exists(name):
        user = UserModel.query.filter(UserModel.name == name).first()
        if not user:
            raise ValidationError('Name not found')

    def user_id_not_exists(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            raise ValidationError('User not found')

    def scenario_id_not_exists(scenario_id):
        scenarioModel = ScenarioModel.query.get(scenario_id)
        if not scenarioModel:
            raise ValidationError('Scenario not found')

    def scenario_id_list_not_exists(scenario_id_list):
        int_scenario_id_list = [int(scenario_id)
                                for scenario_id in scenario_id_list.split(',') if scenario_id]
        for scenario_id in int_scenario_id_list:
            scenarioModel = ScenarioModel.query.get(scenario_id)
            if not scenarioModel:
                raise ValidationError('Scenario not found')

    def type_id_not_exists(type_id):
        typeModel = TypeModel.query.get(type_id)
        if not typeModel:
            raise ValidationError('Type not found')

    def type_id_list_not_exists(type_id_list):
        int_type_id_list = [int(type_id)
                            for type_id in type_id_list.split(',') if type_id]
        for type_id in int_type_id_list:
            typeModel = TypeModel.query.get(type_id)
            if not typeModel:
                raise ValidationError('Type not found')

    def validate_level(level):
        if level is not None and level > 3:
            raise ValidationError("Level must be less than or equal to 3.")
        return level

    def quantity_limited_practice_id_not_exists(id):
        quantity_limited_practice = QuantityLimitedPracticeModel.query.get(id)
        if not quantity_limited_practice:
            raise ValidationError('Record not found')

    def quantity_limited_test_id_not_exists(id):
        quantity_limited_test = QuantityLimitedTestModel.query.get(id)
        if not quantity_limited_test:
            raise ValidationError('Record not found')

    def time_limited_practice_id_not_exists(id):
        time_limited_practice = TimeLimitedPracticeModel.query.get(id)
        if not time_limited_practice:
            raise ValidationError('Record not found')

    def time_limited_test_id_not_exists(id):
        time_limited_test = TimeLimitedTestModel.query.get(id)
        if not time_limited_test:
            raise ValidationError('Record not found')

    def class_name_exists(name):
        class_instance = ClassModel.query.filter(
            ClassModel.name == name).first()
        if class_instance:
            raise ValidationError('Name already exists')

    def class_name_not_exists(name):
        class_instance = ClassModel.query.filter(
            ClassModel.name == name).first()
        if not class_instance:
            raise ValidationError('Name not found')

    def class_id_not_exists(class_id):
        class_instance = ClassModel.query.get(class_id)
        if not class_instance:
            raise ValidationError('Class not found')

    def class_id_list_not_exists(class_id_list):
        if not re.match(r'^[\d,]+$', class_id_list):
            raise ValidationError('class_id_list contains invalid characters')

        int_class_id_list = [int(class_id)
                             for class_id in class_id_list.split(',') if class_id]
        for class_id in int_class_id_list:
            class_instance = ClassModel.query.get(class_id)
            if not class_instance:
                raise ValidationError('Class not found')

    def question_ids_not_exists(question_ids):
        for question_id in question_ids:
            questionModel = QuestionModel.query.get(question_id)
            if not questionModel:
                raise ValidationError('Question not found')

    def question_type_not_exists(question_type):
        questionTypeList = [
            "quantity_limited_practices",
            "quantity_limited_tests",
            "time_limited_practices",
            "time_limited_tests",
        ]
        if question_type not in questionTypeList:
            raise ValidationError('Question type not found')
