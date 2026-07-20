from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import (
    BASE_URL,
    LOGIN_URL
)
from locators import (
    BUTTON_LOGIN_REGISTER,
    INPUT_EMAIL_LOGIN,
    INPUT_PWD_LOGIN,
    BUTTON_LOGIN,
    BUTTON_LOGOUT,
    ELEMENT_AVATAR_USER,
    ELEMENT_USERNAME_DISPLAY
)

class TestUserLogin:

    def test_user_login(self, driver):
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

        avatar_element_locator = ELEMENT_AVATAR_USER
        username_element_locator = ELEMENT_USERNAME_DISPLAY

        avatar_element = wait.until(
            EC.visibility_of_element_located(avatar_element_locator)
        )

        username_element = wait.until(
            EC.visibility_of_element_located(username_element_locator)
        )
        assert username_element.text == "User.", f"Ожидалось имя 'User.', получено '{username_element.text}'"

        logout_button = wait.until(
            EC.element_to_be_clickable(BUTTON_LOGOUT)
        )
        logout_button.click()

        wait.until(lambda d: d.current_url == BASE_URL)