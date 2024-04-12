from test_page_object.pages.base_page import BasePage
from ..data import *

class ForgotPage(BasePage):
    def recover_password(self,
                         driver,
                         locator_button_cabinet,
                         locator_recover_pass,
                         locator_email,
                         locator_button_recover):
        ForgotPage.click_on_element(self, driver, locator_button_cabinet)
        ForgotPage.click_on_element(self, driver, locator_recover_pass)
        ForgotPage.set_text_to_element(self, locator_email, Data.email)
        ForgotPage.click_on_element(self, driver, locator_button_recover)

    def page_recover(self,
                     driver,
                     locator_button_cabinet,
                     locator_recover_pass):
        ForgotPage.click_on_element(self, driver, locator_button_cabinet)
        ForgotPage.click_on_element(self, driver, locator_recover_pass)

    def hide_password(self,
                      driver,
                      locator_button_cabinet,
                      locator_email):
        ForgotPage.click_on_element(self, driver, locator_button_cabinet)
        ForgotPage.click_on_element(self, driver, locator_email)