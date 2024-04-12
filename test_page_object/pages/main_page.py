from test_page_object.pages.base_page import BasePage
from ..data import Data


class MainPage(BasePage):
    def transfer_to_feed(self,
                         driver,
                         locator_feed):
        MainPage.click_on_element(self, driver, locator_feed)

    def transfer_to_constructor(self,
                                driver,
                                locator_feed,
                                locator_cons):
        MainPage.click_on_element(self, driver, locator_feed)
        MainPage.click_on_element(self, driver, locator_cons)

    def new_window(self,
                   driver,
                   locator_element,
                   locator_text):
        MainPage.click_on_element(self, driver, locator_element)
        return MainPage.get_text_from_element(self, locator_text)

    def close_new_window(self,
                         driver,
                         locator_element,
                         locator_close):
        MainPage.click_on_element(self, driver, locator_element)
        MainPage.click_on_element(self, driver, locator_close)


    def add_ingrediend(self,
                       driver,
                       locator_object,
                       locator_base):
        MainPage.drag_drop_element(self, driver, locator_object, locator_base)

    def create_order(self,
                     driver,
                     locator_button_cabinet,
                     locator_email,
                     locator_password,
                     locator_button_entrance,
                     locator_object,
                     locator_base,
                     locator_create_order):
        MainPage.click_on_element(self, driver, locator_button_cabinet)
        MainPage.set_text_to_element(self, locator_email, Data.email)
        MainPage.set_text_to_element(self, locator_password, Data.password)
        MainPage.click_on_element(self, driver, locator_button_entrance)
        MainPage.add_ingrediend(self,
                                driver,
                                locator_object,
                                locator_base)
        MainPage.click_on_element(self, driver, locator_create_order)
