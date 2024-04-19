from test_page_object.pages.base_page import BasePage
from ..data import DataParameters


class ForgotPage(BasePage):
    def recover_password(self,
                         driver,
                         locator_button_cabinet,
                         locator_recover_pass,
                         locator_email,
                         locator_button_recover):
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_recover_pass)
        self.set_text_to_element(locator_email, DataParameters.email)
        self.click_on_element(driver, locator_button_recover)

    def page_recover(self,
                     driver,
                     locator_button_cabinet,
                     locator_recover_pass):
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_recover_pass)

    def hide_password(self,
                      driver,
                      locator_button_cabinet,
                      locator_email):
        self.click_on_element(driver, locator_button_cabinet)
        self.click_on_element(driver, locator_email)
