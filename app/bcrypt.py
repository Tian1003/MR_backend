from flask import Flask
from flask_bcrypt import Bcrypt


bcrypt = None


def bcrypt_init(app: Flask) -> None:
    global bcrypt
    bcrypt = Bcrypt(app)