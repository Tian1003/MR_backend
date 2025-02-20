import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_seeder import FlaskSeeder


def create_app():
    app = Flask(__name__)
    load_dotenv()

    CORS(app, origins=[f"http://127.0.0.1:3000", "http://localhost:3000", os.getenv('DOMAIN')],
         supports_credentials=True)

    if os.getenv('ENV') == "develop":
        app.config.update(
            SESSION_COOKIE_SAMESITE='None',
            SESSION_COOKIE_SECURE='False'
        )

    init_database(app)
    init_bcrypt(app)
    init_seeder(app)
    init_login_manager(app)
    init_principle(app)
    init_blueprints(app)

    return app


def init_database(app: Flask):
    from .database import db_init
    db_init(app)


def init_bcrypt(app: Flask):
    from .bcrypt import bcrypt_init
    bcrypt_init(app)


def init_login_manager(app: Flask):
    from .login_manager import login_manager_init
    login_manager_init(app)


def init_principle(app: Flask):
    from .principle import principle_init
    principle_init(app)


def init_seeder(app: Flask):
    from .database import db
    seeder = FlaskSeeder()
    seeder.init_app(app, db)


def init_blueprints(app: Flask):
    prefix = '/api'
    from .blueprints.auth_blueprint import auth_blueprint
    from .blueprints.student_blueprint import student_blueprint
    from .blueprints.question_blueprint import question_blueprint
    from .blueprints.quantity_limited_practice_blueprint import quantity_limited_practice_blueprint
    from .blueprints.time_limited_practice_blueprint import time_limited_practice_blueprint
    from .blueprints.quantity_limited_test_blueprint import quantity_limited_test_blueprint
    from .blueprints.time_limited_test_blueprint import time_limited_test_blueprint
    from .blueprints.class_blueprint import class_blueprint
    from .blueprints.scenario_question_blueprint import scenario_question_blueprint
    from .blueprints.scenario_practice_blueprint import scenario_practice_blueprint
    from .blueprints.answer_detail_blueprint import answer_detail_blueprint
    app.register_blueprint(auth_blueprint, url_prefix=prefix)
    app.register_blueprint(class_blueprint, url_prefix=prefix)
    app.register_blueprint(student_blueprint, url_prefix=prefix)
    app.register_blueprint(question_blueprint, url_prefix=prefix)
    app.register_blueprint(
        quantity_limited_practice_blueprint, url_prefix=prefix)
    app.register_blueprint(time_limited_practice_blueprint, url_prefix=prefix)
    app.register_blueprint(quantity_limited_test_blueprint, url_prefix=prefix)
    app.register_blueprint(time_limited_test_blueprint, url_prefix=prefix)
    app.register_blueprint(scenario_question_blueprint, url_prefix=prefix)
    app.register_blueprint(scenario_practice_blueprint, url_prefix=prefix)
    app.register_blueprint(answer_detail_blueprint, url_prefix=prefix)
