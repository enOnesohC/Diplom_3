import pytest
import requests
from selenium import webdriver
from test_page_object.urls import URLS
from functions import Functions
import allure


@pytest.fixture(params=["chrome", "firefox"], scope="function", autouse=True)
def browser_driver(request):
    browser = request.param
    if browser == "chrome":
        with allure.step('Открываем браузер Chrome'):
            driver = webdriver.Chrome()
            driver.get(URLS.MAIN_PAGE)
    elif browser == "firefox":
        with allure.step('Открываем браузер Firefox'):
            driver = webdriver.Firefox()
            driver.get(URLS.MAIN_PAGE)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def create_user():
    body = Functions.create_new_user()

    yield body
    body_conf = \
        {
            "email": body[0],
            "password": body[1],
            "name": body[2]
        }
    requests.delete(URLS.URL_DELETE_USER, json=body_conf)
