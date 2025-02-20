import time
from pytest_bdd import scenarios, given, when, then, parsers
from functools import partial
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

scenarios('../features/functional/student_delete.feature')


@given(
    parsers.parse(
        'teacher_account欄位為 {teacher_account}, password欄位為 {password}, target_account欄位為 {target_account}'),
    target_fixture='given_valid_parameters',
)
def given_valid_parameters(teacher_account, password, target_account):
    assert teacher_account in ["teacher"]
    assert password in ["teacher"]
    assert target_account in ["ejtest"]

    return {
        "teacher_account": teacher_account,
        "password": password,
        "target_account": target_account,
    }


@when("前往登入頁面", target_fixture='get_login_page')
def get_login_page(driver, prefix):
    driver.get(f"{prefix}")


@when("輸入 teacher_account 和 password 後點擊登入按鈕", target_fixture='get_login_page')
def type_account_and_password(driver, given_valid_parameters):
    account_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, "account")))
    password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.ID, "password")))

    account_input.send_keys(given_valid_parameters.get("teacher_account"))
    password_input.send_keys(given_valid_parameters.get("password"))

    login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div/div/div/div[1]/div/form/button")))
    login_btn.click()


@when('前往 home 頁面')
def check_url(driver, prefix):
    WebDriverWait(driver, 5).until(
        EC.url_contains(f"{prefix}/home")
    )
    assert driver.current_url == f"{prefix}/home"


@when('點擊「學生帳號」側欄選項')
def when_click_student_tap(driver):
    student_account_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="side"]/div/div/ul/li[3]')))
    student_account_tab.click()


@when('點擊 row data 帳號為測試值的刪除按鈕')
def when_click_delete_btn(driver, given_valid_parameters):
    target_account = given_valid_parameters.get("target_account")

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]')))
    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        if row.find_element(By.XPATH, 'td[4]').text == target_account:
            row.find_element(By.XPATH, 'td[5]/button[2]').click()


@when('點擊「刪除」按鈕')
def when_click_conform_button(driver):
    conform_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/button[1]')))
    conform_button.click()


@then('確認學生列表不存在已被刪除的學生')
def then_check_update_data(driver, given_valid_parameters):
    time.sleep(1)
    is_exist = False
    target_account = given_valid_parameters.get("target_account")

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        if row.find_element(By.XPATH, 'td[4]').text == target_account:
            is_exist = True
            break

    assert is_exist == False
