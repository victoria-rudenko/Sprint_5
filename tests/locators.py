from selenium.webdriver.common.by import By

# Главная страница
BUTTON_LOGIN_REGISTER = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
BUTTON_NO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
BUTTON_CREATE_AD = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")

# Окно логина
INPUT_EMAIL_LOGIN = (By.XPATH, "//input[@name='email']")
INPUT_PWD_LOGIN = (By.XPATH, "//input[@name='password']")
BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")

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
AD_TITLE = (By.XPATH, "//h2[text()='Преступление и Наказание']")

# Окно Чтобы разместить объявление, авторизуйтесь
AUTHORIZATION_REQUIRED_HEADER = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

# Страница создания объявления
INPUT_AD_NAME = (By.XPATH, "//input[@placeholder='Название']")
INPUT_AD_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
INPUT_AD_PRICE = (By.XPATH, "//input[@name='price']")
INPUT_AD_CATEGORY = (By.XPATH, "//input[@name='category']")
INPUT_AD_CITY = (By.XPATH, "//input[@name='city']")
INPUT_AD_CONDITION = (By.XPATH, "//input[@name='condition']")
BUTTON_PUBLISH = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")