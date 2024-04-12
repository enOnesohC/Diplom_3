import time

from test_page_object.pages.base_page import BasePage
from ..data import Data

class ProfilePage(BasePage):

    def transfer_to_cabinet(self,
                            driver,
                            locator_button_cabinet):
        ProfilePage.click_on_element(self, driver, locator_button_cabinet)

    def history_orders(self,
                       driver,
                       locator_button_cabinet,
                       locator_email,
                       locator_password,
                       locator_button_entrance,
                       locator_history):
        ProfilePage.click_on_element(self, driver, locator_button_cabinet)
        ProfilePage.set_text_to_element(self, locator_email, Data.email)
        ProfilePage.set_text_to_element(self, locator_password, Data.password)
        ProfilePage.click_on_element(self, driver, locator_button_entrance)
        time.sleep(2)
        ProfilePage.click_on_element(self, driver, locator_button_cabinet)
        ProfilePage.click_on_element(self, driver, locator_history)

    def authorization_and_exit(self,
                               driver,
                               locator_button_cabinet,
                               locator_email,
                               locator_password,
                               locator_button_entrance,
                               locator_exit):
        ProfilePage.click_on_element(self, driver, locator_button_cabinet)
        ProfilePage.set_text_to_element(self, locator_email, Data.email)
        ProfilePage.set_text_to_element(self, locator_password, Data.password)
        ProfilePage.click_on_element(self, driver, locator_button_entrance)
        time.sleep(2)
        ProfilePage.click_on_element(self, driver, locator_button_cabinet)
        ProfilePage.click_on_element(self, driver, locator_exit)
