from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
from locators import (
    BUTTON_CREATE_AD,
    AUTHORIZATION_REQUIRED_HEADER,
    BUTTON_LOGIN_REGISTER,
    INPUT_EMAIL_LOGIN,
    INPUT_PWD_LOGIN,
    BUTTON_LOGIN,
    INPUT_AD_NAME,
    INPUT_AD_DESCRIPTION,
    INPUT_AD_PRICE,
    INPUT_AD_CATEGORY,
    INPUT_AD_CONDITION,
    INPUT_AD_CITY,
    BUTTON_PUBLISH,
    AD_TITLE
)

class TestAdCreation:
    def test_unauthorized_user_ad_creation(self, driver):
        wait = WebDriverWait(driver, 5)

        driver.get("https://qa-desk.education-services.ru/")
        driver.maximize_window()
        create_ad_button = wait.until(
            EC.element_to_be_clickable(BUTTON_CREATE_AD)
        )
        create_ad_button.click()

        modal_auth_required_element = wait.until(
            EC.visibility_of_element_located(AUTHORIZATION_REQUIRED_HEADER)
        )

        assert modal_auth_required_element.is_displayed(), "Модальное окно 'Авторизация обязательна' не отображается после попытки создания объявления без авторизации."

def safe_action_on_element(driver, wait, condition, action_func, timeout_message=""):
    """
    _________________________________________________________________________________________________
    !!! Коллеги из Яндекс Практикум!!!
    Сайт https://qa-desk.education-services.ru/ КРАЙНЕ НЕСТАБИЛЕН с точки зрения динамического изменения DOM
    сразу после загрузки. JavaScript на странице продолжает активно работать даже после того,
    как document.readyState становится complete, перерисовывая элементы и
    делая ранее найденные элементы "протухшими".

    Cтандартные ожидания не помогают.

    Согласно документации Selenium в разделе "Possible Solutions" для случая "The DOM has changed":
    Always relocate the element every time you go to use it.

    Я реализовала логику повтора попытки найти элемент, если он оказывается "протухшим", с помощью
    цикла while и блока try...except.

    Это было очень трудозатратно, тесты получаются хрупкими,
    прошу пересмотреть реализацию https://qa-desk.education-services.ru/ ,
    чтобы JavaScript не перерисовывал DOM постоянно.
    __________________________________________________________________________________________________
    Функция-обертка для безопасного выполнения действия с элементом,
    обрабатывающая StaleElementReferenceException.

    Args:
        driver: Экземпляр WebDriver.
        wait: Экземпляр WebDriverWait.
        condition: Условие ExpectedConditions для поиска элемента (например, EC.element_to_be_clickable(locator)).
        action_func: Функция, принимающая элемент и выполняющая над ним действие (например, lambda e: e.click()).
        timeout_message: Сообщение для таймаута.

    Returns:
        Найденный WebElement, если действие выполнено успешно.

    Raises:
        TimeoutException: Если действие не выполнено за отведенное время ожидания.
        Другие исключения: Если возникают исключения, кроме StaleElementReferenceException.
    """
    start_time = time.time()
    max_time = start_time + wait._timeout

    while time.time() < max_time:
        try:
            # Повторно ищем элемент каждый раз перед действием
            element = wait.until(condition)
            # Пытаемся выполнить действие
            action_func(element)
            # Если действие прошло успешно, возвращаем элемент
            return element
        except StaleElementReferenceException:
            print(f"Элемент стал протухшим при выполнении действия ('{timeout_message}'), повторный поиск...")
            # Небольшая задержка, чтобы не грузить CPU
            time.sleep(0.1)
            continue  # Переход к следующей итерации цикла для поиска нового элемента
        except Exception as e:
            # Пробрасываем другие исключения, например, TimeoutException от wait.until
            # или исключения от самого action_func, если они не StaleElementReferenceException
            raise e

    # Если цикл завершился по таймауту, выбрасываем исключение
    raise TimeoutException(f"Не удалось выполнить действие за отведённое время ({wait._timeout}s). {timeout_message}")


def test_authorized_user_ad_creation(driver):
    wait = WebDriverWait(driver, 15)

    driver.get("https://qa-desk.education-services.ru/")
    driver.maximize_window()

    # Ожидание полной загрузки начальной страницы
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    # --- Клик по кнопке регистрации/входа ---
    safe_action_on_element(
        driver, wait,
        EC.element_to_be_clickable(BUTTON_LOGIN_REGISTER),
        lambda e: e.click(),
        "Клик по кнопке входа/регистрации"
    )

    # --- Заполнение email ---
    safe_action_on_element(
        driver, wait,
        EC.presence_of_element_located(INPUT_EMAIL_LOGIN),
        lambda e: e.send_keys('abc@bcd.ru'),
        "Заполнение email"
    )

    # --- Заполнение пароля ---
    safe_action_on_element(
        driver, wait,
        EC.presence_of_element_located(INPUT_PWD_LOGIN),
        lambda e: e.send_keys('123'),
        "Заполнение пароля"
    )

    # --- Клик по кнопке "Войти" ---
    safe_action_on_element(
        driver, wait,
        EC.element_to_be_clickable(BUTTON_LOGIN),
        lambda e: e.click(),
        "Клик по кнопке 'Войти'"
    )

    # Ждем, пока страница после входа в систему полностью загрузится.
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    # --- Клик по кнопке создания объявления ---
    create_ad_button = safe_action_on_element(
        driver, wait,
        EC.element_to_be_clickable(BUTTON_CREATE_AD),
        lambda e: e.click(),
        "Клик по кнопке создания объявления"
    )

    # --- Заполнение формы объявления ---

    # Имя объявления
    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(INPUT_AD_NAME),
        lambda e: e.send_keys('Преступление и Наказание'),
        "Заполнение названия объявления"
    )

    # Описание объявления
    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(INPUT_AD_DESCRIPTION),
        lambda e: e.send_keys('Книга в отличном состоянии'),
        "Заполнение описания объявления"
    )

    # Цена объявления
    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(INPUT_AD_PRICE),
        lambda e: e.send_keys('500'),
        "Заполнение цены объявления"
    )

    # Категория объявления
    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(INPUT_AD_CATEGORY),
        lambda e: e.send_keys('Книги'),
        "Заполнение категории объявления"
    )

    ad_condition_selector = INPUT_AD_CONDITION
    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(ad_condition_selector),
        lambda e: e.click(),
        "Клик по переключателю состояния объявления"
    )

    # Город объявления
    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(INPUT_AD_CITY),
        lambda e: e.send_keys('Казань'),
        "Заполнение города объявления"
    )

    # --- Клик по кнопке публикации ---
    publish_button = safe_action_on_element(
        driver, wait,
        EC.element_to_be_clickable(BUTTON_PUBLISH),
        lambda e: e.click(),
        "Клик по кнопке публикации объявления"
    )

    # --- Проверка результата ---
    # Ожидаем возврата на главную страницу
    wait.until(lambda d: d.current_url == "https://qa-desk.education-services.ru/")

    # Повторно ждем загрузки страницы после публикации
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    # Найти элемент заголовка объявления
    ad_title_element = safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(AD_TITLE),
        lambda e: None,  # Ничего не делаем при поиске, только находим
        "Поиск заголовка объявления на главной странице"
    )

    # Проверить, что элемент отображается (это действие тоже может стать причиной StaleElementException)
    # Обернем проверку в ту же логику
    def check_element_displayed(element):
        if not element.is_displayed():
            raise AssertionError("Объявление не опубликовано: элемент заголовка не отображается.")

    safe_action_on_element(
        driver, wait,
        EC.visibility_of_element_located(AD_TITLE),  # Условие снова ищет элемент
        check_element_displayed,  # Функция проверяет отображение
        "Проверка видимости заголовка объявления"
    )
    # Если safe_action_on_element не выбросил исключение, значит проверка прошла.

    print("Тест успешно завершен: объявление опубликовано и видимо на главной странице.")
