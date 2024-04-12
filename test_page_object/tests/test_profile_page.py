import time
import allure
from test_page_object.pages.profile_page import ProfilePage
from test_page_object.locators.main_page_locators import MainPageLocators
from test_page_object.locators.login_page_locators import LoginPageLocators
from test_page_object.locators.profile_page_locators import ProfilePageLocators
from ..urls import URLS


class TestLoginPage:
    @allure.title("Страница авторизации")
    @allure.description("Заходим на главную страницу, переходим на страницу авторизации")
    def test_transfer_to_cabinet(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            profile_page = ProfilePage(browser_driver)
        with allure.step('Клик по кнопке Личный кабинет'):
            profile_page.transfer_to_cabinet(browser_driver, MainPageLocators.PERSONAL_CABINET)
        time.sleep(3)
        with allure.step('Адрес страницы должен быть страницей авторизации'):
            result = browser_driver.current_url
        assert result == URLS.LOGIN_PAGE

    @allure.description("Заходим на главную страницу, переходим на страницу авторизации, авторизуемся, переходим на историю заказов")
    def test_transfer_to_history(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            profile_page = ProfilePage(browser_driver)
        with allure.step('Переходим на страницу авторизации, авторизуемся, переходим на историю заказов'):
            profile_page.history_orders(browser_driver,
                                        MainPageLocators.PERSONAL_CABINET,
                                        LoginPageLocators.EMAIL_FIELD,
                                        LoginPageLocators.PASSWORD_FIELD,
                                        LoginPageLocators.BUTTON_ENTRANCE,
                                        ProfilePageLocators.HISTORY_TEXT)
        time.sleep(3)
        with allure.step('Адрес страницы должен быть страницей истории заказов'):
            result = browser_driver.current_url
        assert result == URLS.ORDER_HISTORY

    @allure.description("Заходим на главную страницу, переходим на страницу авторизации, авторизуемся, выходим")
    def test_auth_and_exit(self, browser_driver):
        with allure.step('Инициализация браузера и переход на стартовую страницу'):
            profile_page = ProfilePage(browser_driver)
        with allure.step('Переходим на страницу авторизации, авторизуемся, выходим'):
            profile_page.authorization_and_exit(browser_driver,
                                                MainPageLocators.PERSONAL_CABINET,
                                                LoginPageLocators.EMAIL_FIELD,
                                                LoginPageLocators.PASSWORD_FIELD,
                                                LoginPageLocators.BUTTON_ENTRANCE,
                                                ProfilePageLocators.EXIT_TEXT)
        time.sleep(3)
        with allure.step('Адрес страницы должен быть страницей авторизации'):
            result = browser_driver.current_url
        assert result == URLS.LOGIN_PAGE
