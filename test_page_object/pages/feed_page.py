import time
from test_page_object.pages.base_page import BasePage
from functions import Functions


class FeedPage(BasePage):
    def click_order_new_window(self,
                               driver,
                               locator_feed,
                               locator_order):
        self.click_on_element(driver, locator_feed)
        self.click_on_element(driver, locator_order)

    def user_orders_in_feed(self,
                            driver,
                            create_user,
                            locator_feed,
                            locator_order,
                            locator_order_number):
        self.click_on_element(driver, locator_feed)

        responce = Functions.create_order_with_auth_with_ingr(create_user)

        order_number = responce.json()['order']['number']
        order_number = str(order_number)

        self.click_on_element(driver, locator_order)

        order_ui = self.get_text_from_element(locator_order_number)
        order_ui = order_ui[2:]

        return order_number, order_ui

    def count_increase(self,
                       driver,
                       create_user,
                       locator_feed,
                       locator_count_total):
        self.click_on_element(driver, locator_feed)

        count_before_order = self.get_text_from_element(locator_count_total)

        Functions.create_order_with_auth_with_ingr(create_user)

        time.sleep(2)
        count_after_order = self.get_text_from_element(locator_count_total)
        return count_before_order, count_after_order

    def number_order_in_progress(self,
                                 driver,
                                 create_user,
                                 locator_feed,
                                 locator_order_progress):
        self.click_on_element(driver, locator_feed)

        responce = Functions.create_order_with_auth_with_ingr(create_user)
        order_ui = self.get_text_from_element(locator_order_progress)

        order_number = responce.json()['order']['number']
        order_number = str(order_number)
        return order_number, order_ui
