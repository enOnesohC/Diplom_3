import time
from test_page_object.locators.login_page_locators import LoginPageLocators
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.pages.forgot_page import ForgotPage
from test_page_object.locators.forgot_page_locators import ForgotPageLocators
from ..urls import *
from ..data import DataClasses
import allure


class TestForgotPage:
    @allure.title("Заходим на главную страницу, переходим на страницу авторизации, проверяем функцию сброса пароля")
    @allure.description("Адрес текущей страницы, после заполнения email и клику по Восстановить должен быть страницей сброса пароля")
    def test_recover_password(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            forgot_page = ForgotPage(browser_driver)
        with allure.step('Переходим на страницу авторизации, проверяем функцию сброса пароля'):
            forgot_page.recover_password(browser_driver,
                                         MainPageLocators.PERSONAL_CABINET,
                                         LoginPageLocators.FORGOT_PASSWORD,
                                         ForgotPageLocators.EMAIL_FIELD,
                                         ForgotPageLocators.BUTTON_RECOVER)
        time.sleep(3)
        with allure.step('Адрес текущей страницы должен быть страницей сброса пароля'):
            result = browser_driver.current_url
        assert result == URLS.RESET_PASSWORD

    @allure.title("Переход по кнопке Забыли пароль")
    @allure.description("При клику по кнопке Забыли пароль должна открыться страница восстановления пароля")
    def test_forgot_page(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            forgot_page = ForgotPage(browser_driver)
        with allure.step('Переход на страницу авторизации, клик по кнопке Забыли пароль'):
            forgot_page.page_recover(browser_driver,
                                     MainPageLocators.PERSONAL_CABINET,
                                     LoginPageLocators.FORGOT_PASSWORD)
        time.sleep(3)
        with allure.step('Адрес текущей страницы должен быть страницей восстановления пароля'):
            result = browser_driver.current_url
        assert result == URLS.FORGOT_PAGE

    @allure.title("Поле Email при клике должно подсвечиваться при клике")
    @allure.description("После клика по полю Email сравняем класс поля с эталонным: " + DataClasses.tab_class)
    def test_hide_password(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            forgot_page = ForgotPage(browser_driver)
        with allure.step('Переход на страницу авторизации и клик по полю EMAIL'):
            forgot_page.hide_password(browser_driver,
                                      MainPageLocators.PERSONAL_CABINET,
                                      ForgotPageLocators.EMAIL_FIELD)
        with allure.step('Поиск элемента, получение его класса и сравнение с эталоном'):
            element = browser_driver.find_element(*ForgotPageLocators.EMAIL_FIELD)
            tab = element.find_element(*LoginPageLocators.EMAIL_FIELD_ACTIVE)
            tab_class = tab.get_attribute("class")
        assert tab_class == DataClasses.tab_class
