from selenium.webdriver.common.by import By


class ProfilePageLocators:
    HISTORY_TEXT = By.XPATH, "//a[text()='История заказов']"
    EXIT_TEXT = By.XPATH, "//button[text()='Выход']"
