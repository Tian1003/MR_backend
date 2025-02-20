from dotenv import load_dotenv
from flask import Blueprint, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from flask_principal import Identity, identity_changed
from marshmallow import ValidationError
from app.bcrypt import bcrypt
from ..models.user_model import UserModel
from ..validation.student_login_schema import StudentLoginSchema
from ..validation.teacher_login_schema import TeacherLoginSchema
from ..utilities.api_response_helper import make_success_response, make_error_response

auth_blueprint = Blueprint('auth_blueprint', __name__)
load_dotenv()


@auth_blueprint.route('/me', methods=['GET'])
@login_required
def me():
    try:
        return make_success_response(None, 200)
    except Exception as err:
        return make_error_response(err, 400)


@auth_blueprint.route('/teacher/login', methods=['POST'])
def teacher_login():
    data = request.json
    messages = []

    try:
        validated_data = TeacherLoginSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    account = validated_data.get('account')
    password = validated_data.get('password')

    user = UserModel.query.filter(UserModel.account == account).first()
    if (account == user.account and bcrypt.check_password_hash(user.password, password)):
        user = UserModel.query.filter(UserModel.id == user.id).first()

        login_user(user)
        identity_changed.send(current_app._get_current_object(),
                              identity=Identity(user.id))
        return make_success_response(user.serialize(), 200)
    else:
        messages.append({
            "account": 'Invalid account or password'
        })
        return make_error_response(messages, 400)


@auth_blueprint.route('/student/login', methods=['POST'])
def student_login():
    data = request.json
    messages = []

    try:
        validated_data = StudentLoginSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)

    account = validated_data.get('account')

    try:
        user = UserModel.query.filter(UserModel.account == account).first()
        login_user(user)
        identity_changed.send(current_app._get_current_object(),
                              identity=Identity(user.id))
        return make_success_response(user.serialize(), 200)
    except Exception as err:
        return make_error_response(err, 400)


@auth_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    identity_changed.send(current_app._get_current_object(),
                          identity=Identity(None))
    return make_success_response(None, 200)
