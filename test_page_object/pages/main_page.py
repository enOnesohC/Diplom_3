from test_page_object.pages.base_page import BasePage
from ..data import DataParameters


class MainPage(BasePage):
    def transfer_to_feed(self,
                         driver,
                         locator_feed):
        self.click_on_element(driver, locator_feed)

    def transfer_to_constructor(self,
                                driver,
                                locator_feed,
                                locator_cons):
        self.click_on_element(driver, locator_feed)
        self.click_on_element(driver, locator_cons)

    def new_window(self,
                   driver,
                   locator_element,
                   locator_text):
        self.click_on_element(driver, locator_element)
        return self.get_text_from_element(locator_text)

    def close_new_window(self,
                         driver,
                         locator_element,
                         locator_close):
        self.click_on_element(driver, locator_element)
        self.click_on_element(driver, locator_close)

    def add_ingrediend(self,
                       driver,
                       locator_object,
                       locator_base):
        self.drag_drop_element(driver, locator_object, locator_base)

    def create_order(self,
                     driver,
                     locator_button_cabinet,
                     locator_email,
                     locator_password,
                     locator_button_entrance,
                     locator_object,
                     locator_base,
                     locator_create_order):
        self.click_on_element(driver, locator_button_cabinet)
        self.set_text_to_element(locator_email, DataParameters.email)
        self.set_text_to_element(locator_password, DataParameters.password)
        self.click_on_element(driver, locator_button_entrance)
        self.add_ingrediend(driver,
                            locator_object,
                            locator_base)
        self.click_on_element(driver, locator_create_order)
