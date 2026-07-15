from selenium.webdriver.common.by import By

# Главная страница
BUTTON_LOGIN_REGISTER = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
BUTTON_NO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")

# Окно регистрации
INPUT_EMAIL_REGISTRATION = (By.NAME, "email")
INPUT_PASSWORD_REGISTRATION = (By.NAME, "password")
INPUT_SUBMIT_PASSWORD_REGISTRATION = (By.NAME, "submitPassword")
BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[@type='submit' and contains(., 'Создать')]")
ERROR_MESSAGE = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/form/div[2]/div[1]/span")

# После успешной регистрации
ELEMENT_AVATAR_USER = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/button")
ELEMENT_USERNAME_DISPLAY = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div/h3")
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выйти')]")