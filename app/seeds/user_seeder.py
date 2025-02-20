import os
import random
from dotenv import load_dotenv
from app.models.user_model import UserModel
from app.database import db
from app.bcrypt import bcrypt
from .base_seeder import BaseSeeder


class UserSeeder(BaseSeeder):
    def run(self):
        load_dotenv()
        hashed_password = bcrypt.generate_password_hash(password="teacher")

        teacher = UserModel(
            account="teacher",
            name="teacher",
            password=hashed_password
        )
        db.session.add(teacher)

        hashed_password = bcrypt.generate_password_hash(password="developer")
        developer = UserModel(
            account="developer",
            name="developer",
            password=hashed_password
        )
        db.session.add(developer)

        if (os.getenv('ENV') == 'develop'):
            for _ in range(10):
                random_numbers = [str(random.randint(0, 9)) for _ in range(4)]
                studnet = UserModel(
                    class_id=random.randint(1, 5),
                    account=f"s112{''.join(random_numbers)}",
                    name=self.faker.name(),
                )
                db.session.add(studnet)

            db.session.commit()

        print("users added")
