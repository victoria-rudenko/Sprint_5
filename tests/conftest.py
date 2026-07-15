import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver_instance = webdriver.Chrome()
    yield driver_instance
    driver_instance.quit()