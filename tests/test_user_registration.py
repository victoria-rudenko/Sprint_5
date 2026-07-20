from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils import email_generator
from constants import *
from locators import (
    BUTTON_LOGIN_REGISTER,
    BUTTON_NO_ACCOUNT,
    INPUT_EMAIL_REGISTRATION,
    INPUT_PASSWORD_REGISTRATION,
    INPUT_SUBMIT_PASSWORD_REGISTRATION,
    BUTTON_CREATE_ACCOUNT,
    ELEMENT_AVATAR_USER,
    ELEMENT_USERNAME_DISPLAY,
    ERROR_MESSAGE,
    BUTTON_LOGOUT
)

class TestUserRegistration:

    def test_user_registration(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.get(BASE_URL)
        driver.maximize_window()
        login_register_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_LOGIN_REGISTER)
        )
        login_register_button.click()
        no_account_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_NO_ACCOUNT)
        )
        no_account_button.click()
        email = email_generator()
        password = "TestPassword123!"
        email_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_EMAIL_REGISTRATION)
        )
        email_field.send_keys(email)
        password_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_PASSWORD_REGISTRATION)
        )
        password_field.send_keys(password)
        submit_password_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_SUBMIT_PASSWORD_REGISTRATION)
        )
        submit_password_field.send_keys(password)
        create_account_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_CREATE_ACCOUNT)
        )
        create_account_button.click()

        wait.until(lambda d: d.current_url == REGISTRATION_URL)

        avatar_element_locator = ELEMENT_AVATAR_USER
        username_element_locator = ELEMENT_USERNAME_DISPLAY

        avatar_element = wait.until(
            expected_conditions.visibility_of_element_located(avatar_element_locator)
        )

        username_element = wait.until(
            expected_conditions.visibility_of_element_located(username_element_locator)
        )
        assert username_element.text == "User.", f"Ожидалось имя 'User.', получено '{username_element.text}'"

    def test_incorrect_email_user_registration(self, driver):
        wait = WebDriverWait(driver, 10)

        driver.get(BASE_URL)
        driver.maximize_window()
        login_register_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_LOGIN_REGISTER)
        )
        login_register_button.click()
        no_account_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_NO_ACCOUNT)
        )
        no_account_button.click()
        email = email_generator().replace("@", "") # проверка для сценария, когда email не содержит @
        password = "TestPassword123!"
        email_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_EMAIL_REGISTRATION)
        )
        email_field.send_keys(email)
        password_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_PASSWORD_REGISTRATION)
        )
        password_field.send_keys(password)
        submit_password_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_SUBMIT_PASSWORD_REGISTRATION)
        )
        submit_password_field.send_keys(password)
        create_account_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_CREATE_ACCOUNT)
        )
        create_account_button.click()

        error_element = wait.until(
            expected_conditions.visibility_of_element_located(ERROR_MESSAGE)
        )

        assert error_element.text == "Ошибка", f"Ожидалась ошибка при некорректном email для регистрации"

    def test_existing_user_registration(self, driver):
        wait = WebDriverWait(driver, 5)

        # Сначала регистрируем нового пользователя
        driver.get(BASE_URL)
        driver.maximize_window()
        login_register_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_LOGIN_REGISTER)
        )
        login_register_button.click()
        no_account_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_NO_ACCOUNT)
        )
        no_account_button.click()
        email = email_generator()
        password = "TestPassword123!"
        email_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_EMAIL_REGISTRATION)
        )
        email_field.send_keys(email)
        password_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_PASSWORD_REGISTRATION)
        )
        password_field.send_keys(password)
        submit_password_field = wait.until(
            expected_conditions.presence_of_element_located(INPUT_SUBMIT_PASSWORD_REGISTRATION)
        )
        submit_password_field.send_keys(password)
        create_account_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_CREATE_ACCOUNT)
        )
        create_account_button.click()

        wait.until(lambda d: d.current_url == REGISTRATION_URL)

        avatar_element_locator = ELEMENT_AVATAR_USER
        username_element_locator = ELEMENT_USERNAME_DISPLAY

        wait.until(
            expected_conditions.visibility_of_element_located(avatar_element_locator)
        )

        wait.until(
            expected_conditions.visibility_of_element_located(username_element_locator)
        )

        logout_button = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_LOGOUT)
        )
        logout_button.click()

        # Пытаемся снова зарегистрироваться под тем же пользователем
        login_register_retry = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_LOGIN_REGISTER)
        )
        login_register_retry.click()
        no_account_retry = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_NO_ACCOUNT)
        )
        no_account_retry.click()
        email_field_retry = wait.until(
            expected_conditions.presence_of_element_located(INPUT_EMAIL_REGISTRATION)
        )
        email_field_retry.send_keys(email)
        password_field_retry = wait.until(
            expected_conditions.presence_of_element_located(INPUT_PASSWORD_REGISTRATION)
        )
        password_field_retry.send_keys(password)
        submit_password_retry = wait.until(
            expected_conditions.presence_of_element_located(INPUT_SUBMIT_PASSWORD_REGISTRATION)
        )
        submit_password_retry.send_keys(password)
        create_account_retry = wait.until(
            expected_conditions.element_to_be_clickable(BUTTON_CREATE_ACCOUNT)
        )
        create_account_retry.click()
        error_element_retry = wait.until(
            expected_conditions.visibility_of_element_located(ERROR_MESSAGE)
        )
        assert error_element_retry.text == "Ошибка", f"Ожидалась ошибка при попытке регистрации существующего пользователя"