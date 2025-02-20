from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


scenarios('../features/functional/auth.feature')


@given(
    parsers.parse('account欄位為 {account}, password欄位為 {password}'),
    target_fixture='given_valid_account_password',
    converters={
        'account': str
    }
)
def given_valid_account_password(account, password):
    assert account in ["teacher"]
    assert password in ["teacher"]

    return {
        "account": account,
        "password": password
    }


@when("前往登入頁面", target_fixture='get_login_page')
def get_login_page(driver, prefix):
    driver.get(f"{prefix}")


@when("輸入 account 和 password 後點擊登入按鈕", target_fixture='get_login_page')
def type_account_and_password(driver, given_valid_account_password):
    account_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "account")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "password")))

    account_input.send_keys(given_valid_account_password.get("account"))
    password_input.send_keys(given_valid_account_password.get("password"))

    login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div/div/div[1]/div/form/button")))
    login_btn.click()


@then('前往 home 頁面')
def then_check_response(driver, prefix):
    WebDriverWait(driver, 5).until(
        EC.url_contains(f"{prefix}/home")
    )
    assert driver.current_url == f"{prefix}/home"
