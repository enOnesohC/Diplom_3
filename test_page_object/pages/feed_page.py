import time
from test_page_object.pages.base_page import BasePage


class FeedPage(BasePage):
    def click_order_new_window(self,
                               driver,
                               locator_feed,
                               locator_order):
        FeedPage.click_on_element(self, driver, locator_feed)
        FeedPage.click_on_element(self, driver, locator_order)

    def user_orders_in_feed(self,
                            driver,
                            create_user,
                            locator_feed,
                            locator_order,
                            locator_order_number):
        FeedPage.click_on_element(self, driver, locator_feed)

        responce = BasePage.create_order_with_auth_with_ingr(self, create_user)

        order_number = responce.json()['order']['number']
        order_number = str(order_number)

        FeedPage.click_on_element(self, driver, locator_order)

        order_ui = FeedPage.get_text_from_element(self, locator_order_number)
        order_ui = order_ui[2:]

        return order_number, order_ui

    def count_increase(self,
                         driver,
                         create_user,
                         locator_feed,
                         locator_count_total):
        FeedPage.click_on_element(self, driver, locator_feed)

        count_before_order = FeedPage.get_text_from_element(self, locator_count_total)

        BasePage.create_order_with_auth_with_ingr(self, create_user)
        time.sleep(2)
        count_after_order = FeedPage.get_text_from_element(self, locator_count_total)
        return count_before_order, count_after_order

    def number_order_in_progress(self,
                                 driver,
                                 create_user,
                                 locator_feed,
                                 locator_order_progress):
        FeedPage.click_on_element(self, driver, locator_feed)

        responce = BasePage.create_order_with_auth_with_ingr(self, create_user)
        order_ui = FeedPage.get_text_from_element(self, locator_order_progress)

        order_number = responce.json()['order']['number']
        order_number = str(order_number)
        return order_number, order_ui


