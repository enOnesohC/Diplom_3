import time
from test_page_object.pages.base_page import BasePage
from ..data import DataParameters


class ProfilePage(BasePage):

    def transfer_to_cabinet(self,
                            driver,
                            locator_button_cabinet):
        self.click_on_element(driver, locator_button_cabinet)

    def history_orders(self,
                       driver,
                       locator_button_cabinet,
                       locator_email,
                       locator_password,
                       locator_button_entrance,
                       locator_history):
        self.click_on_element(driver, locator_button_cabinet)
        self.set_text_to_element(locator_email, DataParameters.email)
        self.set_text_to_element(locator_password, DataParameters.password)
        self.click_on_element(driver, locator_button_entrance)
        time.sleep(2)
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_history)

    def authorization_and_exit(self,
                               driver,
                               locator_button_cabinet,
                               locator_email,
                               locator_password,
                               locator_button_entrance,
                               locator_exit):
        self.click_on_element(driver, locator_button_cabinet)
        self.set_text_to_element(locator_email, DataParameters.email)
        self.set_text_to_element(locator_password, DataParameters.password)
        self.click_on_element(driver, locator_button_entrance)
        time.sleep(2)
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_exit)
