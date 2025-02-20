import pytest
import os
import sys
sys.path.append(".")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture(scope='session')
def prefix():
    return f"http://{os.getenv('HOST')}:{os.getenv('FRONTEND_PORT')}"


@pytest.fixture(scope='session')
def app():
    from app import create_app

    test_app = create_app()
    return test_app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def driver():
    # options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    # options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    #                      f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

    options = webdriver.ChromeOptions()
    service=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()