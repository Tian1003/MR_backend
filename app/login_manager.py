import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from .models.user_model import UserModel

login_manager = None


def login_manager_init(app: Flask) -> None:
    global login_manager
    load_dotenv()
    app.secret_key = os.getenv('SECRET_KEY')
    login_manager = LoginManager(app)
    login_manager.init_app(app)

    @login_manager.request_loader
    def load_user_from_request(request):
        print(request)

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.filter(UserModel.id == int(user_id)).first()
