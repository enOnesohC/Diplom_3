from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
import requests
from test_page_object.urls import URLS


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        (WebDriverWait(self.driver, 5).
         until(expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    def click_on_element(self, browser, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #не работает в firefox, поэтому кликаем через скрипт
        #element.click()
        browser.execute_script("arguments[0].click();", element)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.send_keys(text)

    def drag_drop_element(self, driver, locator_start, locator_final):
        element_start = self.find_element_with_wait(locator_start)
        element_final = self.find_element_with_wait(locator_final)

        drag_and_drop(driver, element_start, element_final)

    def create_order_with_auth_with_ingr(self, create_user):
        header = \
            {
                'Authorization': create_user[3]
            }

        body = \
            {
                "email": create_user[0],
                "password": create_user[1],
                "name": create_user[2]
            }
        requests.post(URLS.URL_AUTHORIZATION, json=body, headers=header)

        responce_ingredients = requests.get(URLS.URL_CREATE_ORDER)
        ingredients = responce_ingredients.json()["data"]

        body_order = \
            {
                "ingredients": [ingredients[0]["_id"], ingredients[1]["_id"]]
            }

        responce = requests.post(URLS.URL_GET_ORDERS_USER, json=body_order, headers=header)
        return responce
