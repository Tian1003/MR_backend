import os
from app import create_app
from dotenv import load_dotenv

app = None

if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run(host=os.getenv('HOST'), port=os.getenv('BACKEND_PORT'))
