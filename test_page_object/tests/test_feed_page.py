from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.feed_page import FeedPage
from test_page_object.locators.feed_page_locators import FeedPageLocators
import allure


class TestFeedPage:
    @allure.title("При клике по заказу открывается окно информацией заказа")
    @allure.description("Кликаем по заказу и проверяем, что номер в окне заказа не пустой")
    def test_click_order_new_window(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            feed_page = FeedPage(browser_driver)
        with allure.step('Переход на Ленту заказов, клик по первому заказу'):
            feed_page.click_order_new_window(browser_driver, MainPageLocators.FEED_TEXT,
                                             FeedPageLocators.ORDERS_1)
        with allure.step('Получение номера заказа в окне заказа'):
            element = browser_driver.find_element(*FeedPageLocators.ORDERS_1_NUMBER)
        assert element.text != ""

    @allure.title("Заказы пользователя отображаются в Ленте заказов")
    @allure.description("Делаем заказ, получаем номер заказа, сверяем полученный номер заказа с номером первого заказа в Ленте заказов")
    def test_user_orders_in_feed(self, browser_driver, create_user):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            feed_page = FeedPage(browser_driver)
        with allure.step('Формирование заказа с помощью api, клик по первому заказу, получение номера заказа'):
            order_responce, order_ui = feed_page.user_orders_in_feed(browser_driver,
                                                                     create_user,
                                                                     MainPageLocators.FEED_TEXT,
                                                                     FeedPageLocators.ORDERS_1,
                                                                     FeedPageLocators.ORDERS_1_NUMBER)
        assert order_responce == order_ui

    @allure.title("Счётчик всех заказов при создании заказа увеличивается на 1")
    @allure.description("Получаем количество всех заказов, делаем заказ, получаем номер заказа, проверяем что разница между ними равна 1")
    def test_total_count(self, browser_driver, create_user):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            feed_page = FeedPage(browser_driver)

        with allure.step('Переход на Ленту заказов, создание заказа через api, получение счётчика'):
            count_before_order, count_after_order = feed_page.count_increase(browser_driver,
                                                                             create_user,
                                                                             MainPageLocators.FEED_TEXT,
                                                                             FeedPageLocators.TOTAL_COUNT_ORDER)

        assert int(count_after_order) == int(count_before_order) + 1

    @allure.title("Счётчик заказов за день при создании заказа увеличивается на 1")
    @allure.description("Получаем количество заказов за день, делаем заказ, получаем номер заказа, проверяем что разница между ними равна 1")
    def test_day_count(self, browser_driver, create_user):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            feed_page = FeedPage(browser_driver)
        with allure.step('Переход на Ленту заказов, создание заказа через api, получение счётчика'):
            count_before_order, count_after_order = feed_page.count_increase(browser_driver,
                                                                             create_user,
                                                                             MainPageLocators.FEED_TEXT,
                                                                             FeedPageLocators.DAY_COUNT_ORDER)

        assert int(count_after_order) == int(count_before_order) + 1

    @allure.title("При создании заказа отображается номер заказа, который в работе")
    @allure.description("Делаем заказ, получаем номер заказа, который должен быть равен номеру заказа в работе")
    def test_number_order(self, browser_driver, create_user):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            feed_page = FeedPage(browser_driver)
        with allure.step('Переход на Ленту заказов, создание заказа через api, получение номера заказа, который в работе'):
            order_number, order_ui = feed_page.number_order_in_progress(browser_driver,
                                                                        create_user,
                                                                        MainPageLocators.FEED_TEXT,
                                                                        FeedPageLocators.CURRENT_ORDER)
        with allure.step('Преобразование номера заказа для сравнения'):
            order_ui = order_ui[1:]
        assert order_number == order_ui
