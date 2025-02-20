def _drop_all_tables(app, db):
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.session.commit()
        db.session.close()
        print("Database dropped")


def _create_all_tables(app, db):
    with app.app_context():
        import app.models.system_parameter_model
        import app.models.class_model
        import app.models.user_model
        import app.models.type_model
        import app.models.question_model
        import app.models.quantity_limited_practice_model
        import app.models.quantity_limited_test_model
        import app.models.time_limited_practice_model
        import app.models.time_limited_test_model
        import app.models.scenario_model
        import app.models.scenario_element_model
        import app.models.scenario_question_model
        import app.models.scenario_practice_model
        import app.models.answer_detail_model
        db.reflect()
        db.create_all()
        db.session.commit()
        db.session.close()
        print("Database created")


def init_database(app, db):
    with app.app_context():
        if (os.getenv('ENV') == 'develop'):
            _drop_all_tables(app, db)
        _create_all_tables(app, db)


def run_seeder(entry):
    from app.seeds.system_parameter_seeder import SystemParameterSeeder
    from app.seeds.class_seeder import ClassSeeder
    from app.seeds.user_seeder import UserSeeder
    from app.seeds.type_seeder import TypeSeeder
    from app.seeds.question_seeder import QuestionSeeder
    from app.seeds.quantity_limited_practice_seeder import QuantityLimitedPracticeSeeder
    from app.seeds.quantity_limited_test_seeder import QuantityLimitedTestSeeder
    from app.seeds.time_limited_practice_seeder import TimeLimitedPracticeSeeder
    from app.seeds.time_limited_test_seeder import TimeLimitedTestSeeder
    from app.seeds.scenario_seeder import ScenarioSeeder
    from app.seeds.scenario_element_seeder import ScenarioElementSeeder
    from app.seeds.scenario_question_seeder import ScenarioQuestionSeeder
    from app.seeds.scenario_practice_seeder import ScenarioPracticeSeeder
    from app.seeds.answer_detail_seeder import AnswerDetailSeeder

    with app.app_context():
        SystemParameterSeeder().run()
        ClassSeeder().run()
        UserSeeder().run()
        TypeSeeder().run()
        QuestionSeeder(entry).run()
        QuantityLimitedPracticeSeeder().run()
        QuantityLimitedTestSeeder().run()
        TimeLimitedPracticeSeeder().run()
        TimeLimitedTestSeeder().run()
        ScenarioSeeder().run()
        ScenarioElementSeeder().run()
        ScenarioQuestionSeeder().run()
        ScenarioPracticeSeeder().run()
        AnswerDetailSeeder().run()

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    if (os.getenv('ENV') != 'develop'):
        account = input("Who am I: ")
        secret = input("Secret: ")

        # Do not reset db in prod!!
        if account != "root" or secret != "qtds":
            print("Invalid account or secret. Exiting...")
            exit()

    try:
        import sys
        from flask import Flask

        print("create app")
        app = Flask(__name__)

        from app.database import db_init
        db_init(app)
        from app.database import db

        from app.bcrypt import bcrypt_init
        bcrypt_init(app)

        entry = os.path.dirname(os.path.realpath(__name__))

        init_database(app, db)
        run_seeder(entry)
        print("Database initialized")
    except Exception as e:
        print("An error occurred:", e)

    if (os.getenv('ENV') != 'develop'):
        input("Press Enter to exit...")
        sys.exit(1)
