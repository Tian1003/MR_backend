import time
from pytest_bdd import scenarios, given, when, then, parsers
from functools import partial
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

scenarios('../features/functional/student_update.feature')


@given(
    parsers.parse(
        'teacher_account欄位為 {teacher_account}, password欄位為 {password}, student_name欄位為 {student_name}, student_account欄位為 {student_account}, student_origin_account欄位為 {student_origin_account}'),
    target_fixture='given_valid_parameters',
)
def given_valid_parameters(teacher_account, password, student_name, student_account, student_origin_account):
    assert teacher_account in ["teacher"]
    assert password in ["teacher"]
    assert student_name in ["ejtest"]
    assert student_account in ["ejtest"]
    assert student_origin_account in ["ejj"]

    return {
        "teacher_account": teacher_account,
        "password": password,
        "student_name": student_name,
        "student_account": student_account,
        "student_origin_account": student_origin_account,
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


@when('點擊 row data 帳號為測試值的更新按鈕')
def when_click_update_btn(driver, given_valid_parameters):
    student_account = given_valid_parameters.get("student_origin_account")

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]')))
    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        if row.find_element(By.XPATH, 'td[4]').text == student_account:
            row.find_element(By.XPATH, 'td[5]/button[1]').click()


@when('在「姓名」輸入框測試值')
def when_input_name(driver, given_valid_parameters):
    name_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/form/div[1]/input')))
    name_input.send_keys(Keys.CONTROL + "a")
    name_input.send_keys(Keys.DELETE)
    # name_input.clear()
    name_input.send_keys(given_valid_parameters.get("student_name"))


@when('在「帳號」輸入框測試值')
def when_input_account(driver, given_valid_parameters):
    account_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/form/div[2]/input')))
    account_input.send_keys(Keys.CONTROL + "a")
    account_input.send_keys(Keys.DELETE)
    # account_input.clear()
    account_input.send_keys(given_valid_parameters.get("student_account"))


@when('選擇「班級」下拉選單第二個選項')
def when_choose_class_drop_down(driver):
    class_select = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/form/div[3]/select')))
    class_select.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/form/div[3]/select/option[2]')))
    class_select = Select(class_select)
    class_select.select_by_index(2)


@when('點擊「修改」按鈕')
def when_click_conform_button(driver):
    conform_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[3]/div/div/div/form/div[4]/button[2]')))
    conform_button.click()


@then('確認學生列表有此更新後的學生')
def then_check_update_data(driver, given_valid_parameters):
    time.sleep(1)
    is_exist = False
    student_name = given_valid_parameters.get("student_name")
    student_account = given_valid_parameters.get("student_account")

    tbody = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="global"]/div[2]/div[2]/div[2]/div/div[2]/table/tbody')))
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        if row.find_element(By.XPATH, 'td[3]').text == student_name and row.find_element(By.XPATH, 'td[4]').text == student_account:
            is_exist = True
            break

    assert is_exist == True
