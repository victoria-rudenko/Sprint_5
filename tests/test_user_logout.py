from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL, LOGIN_URL
from locators import (
    BUTTON_LOGIN_REGISTER,
    INPUT_EMAIL_LOGIN,
    INPUT_PWD_LOGIN,
    BUTTON_LOGIN
)

class TestUserLogout:

    def test_user_logout(self, driver):
        wait = WebDriverWait(driver, 15)

        driver.get(BASE_URL)
        driver.maximize_window()

        # Ожидание полной загрузки начальной страницы
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        login_register_button = wait.until(
            EC.element_to_be_clickable(BUTTON_LOGIN_REGISTER)
        )
        login_register_button.click()

        email_login_input = wait.until(
            EC.presence_of_element_located(INPUT_EMAIL_LOGIN)
        )
        email_login_input.send_keys("abc@bcd.ru")
        password_input = wait.until(
            EC.presence_of_element_located(INPUT_PWD_LOGIN)
        )
        password_input.send_keys("123")

        login_register_button = wait.until(
            EC.element_to_be_clickable(BUTTON_LOGIN)
        )
        login_register_button.click()

        wait.until(lambda d: d.current_url == LOGIN_URL)

        login_button = wait.until(
            EC.element_to_be_clickable(BUTTON_LOGIN_REGISTER)
        )
        assert login_button is not None, "Кнопка 'Вход и регистрация' не найдена или не кликабельна в конце теста."