import time
from test_page_object.locators.login_page_locators import LoginPageLocators
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.main_page import MainPage
from ..urls import *
from ..data import Data
import allure


class TestMainPage:
    @allure.title("Главная страница")
    @allure.description("Заходим на главную страницу, переходим на страницу Лента заказов")
    def test_transfer_to_feed(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            main_page = MainPage(browser_driver)
        with allure.step('Клик по полю Лента заказов'):
            main_page.transfer_to_feed(browser_driver, MainPageLocators.FEED_TEXT)
        time.sleep(3)
        with allure.step('Текущий адрес страницы должен быть адресом Ленты заказов'):
            result = browser_driver.current_url
        assert result == URLS.FEED_PAGE

    @allure.description("Заходим на главную страницу, переходим на страницу Лента заказов, переходим на страницу Конструктор заказов")
    def test_transfer_to_cons(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            main_page = MainPage(browser_driver)
        with allure.step('Переходим на страницу Лента заказов, переходим на страницу Конструктор заказов'):
            main_page.transfer_to_constructor(browser_driver,
                                              MainPageLocators.FEED_TEXT,
                                              MainPageLocators.CONSTRUCTOR_TEXT)
        time.sleep(3)
        with allure.step('Текущий адрес страницы должен быть адресом Конструктора заказов'):
            result = browser_driver.current_url
        assert result == URLS.MAIN_PAGE

    @allure.description("При клике по ингредиенту открывается его карточка")
    def test_new_window(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            main_page = MainPage(browser_driver)
        with allure.step('Клик по ингредиенту и проверка открытия карточки'):
            result = main_page.new_window(browser_driver,
                                          MainPageLocators.OBJECT_ORDER,
                                          MainPageLocators.WINDOW_OBJECT)
        assert result == Data.result

    @allure.description("Клик по ингредиенту и закрытие его карточки")
    def test_close_new_window(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            main_page = MainPage(browser_driver)
        with allure.step('Клик по ингредиенту и клик по кнопке закрытия карточки'):
            main_page.close_new_window(browser_driver,
                                       MainPageLocators.OBJECT_ORDER,
                                       MainPageLocators.WINDOW_BUTTON_CLASS)
        with allure.step('Поиск элемента и сравнение его класса с эталонным значением'):
            element = browser_driver.find_element(*MainPageLocators.SECTION_CLASS)
            element_class = element.get_attribute("class")
        assert element_class == Data.element_class

    @allure.description("Добавление ингредиента в заказ")
    def test_add_ingredient(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            main_page = MainPage(browser_driver)
        with allure.step('drag-and-drop ингредиент в корзину'):
            main_page.add_ingrediend(browser_driver,
                                     MainPageLocators.OBJECT_ORDER,
                                     MainPageLocators.BASE_ORDER)
        with allure.step('Ищем цену и убеждаемся, что там не 0'):
            element = browser_driver.find_element(*MainPageLocators.TOTAL_PRICE)
        assert element.text != "0"

    @allure.description("Авторизуемся, создаём заказ, получаем номер заказа")
    def test_create_order(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            main_page = MainPage(browser_driver)
        with allure.step('Авторизация, создание заказа, получение номера заказа'):
            main_page.create_order(browser_driver,
                                   MainPageLocators.PERSONAL_CABINET,
                                   LoginPageLocators.EMAIL_FIELD,
                                   LoginPageLocators.PASSWORD_FIELD,
                                   LoginPageLocators.BUTTON_ENTRANCE,
                                   MainPageLocators.OBJECT_ORDER,
                                   MainPageLocators.BASE_ORDER,
                                   MainPageLocators.BUTTON_ORDER)
        with allure.step('Номер заказа не должен быть пустым значением'):
            element = browser_driver.find_element(*MainPageLocators.ORDER_NUMBER)
        assert element.text != ""
