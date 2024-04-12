from selenium.webdriver.common.by import By


class ForgotPageLocators:
    EMAIL_FIELD = By.XPATH, "//input[@name='name']"
    BUTTON_RECOVER = By.XPATH, "//button[text()='Восстановить']"
