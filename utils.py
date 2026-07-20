import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import random
import string

def safe_action_on_element(driver, wait, condition, action_func, timeout_message=""):
    """
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
            continue  # Переход к следующей итерации цикла для поиска нового элемента
        except Exception as e:
            # Пробрасываем другие исключения, например, TimeoutException от wait.until
            # или исключения от самого action_func, если они не StaleElementReferenceException
            raise e

    # Если цикл завершился по таймауту, выбрасываем исключение
    raise TimeoutException(f"Не удалось выполнить действие за отведённое время ({wait._timeout}s). {timeout_message}")

def email_generator():
    # Генерация случайного email соответствующего маске *******@*******.***
    random_name = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=7))
    random_domain = ''.join(random.choices(string.ascii_lowercase, k=3))
    return f"{random_name}@{random_name}.{random_domain}"

def check_element_displayed(element):
    if not element.is_displayed():
        raise AssertionError("Объявление не опубликовано: элемент заголовка не отображается.")