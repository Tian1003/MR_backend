import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = None


def db_init(app: Flask) -> None:
    global db
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_ACCOUNT')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('SCHEMA_NAME')}"
    db = SQLAlchemy(app)
