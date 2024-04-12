from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    EMAIL_FIELD = By.XPATH, "//input[@type='text']"
    PASSWORD_FIELD = By.XPATH, "//input[@type='password']"
    BUTTON_ENTRANCE = By.XPATH, "//button[text()='Войти']"
    BUTTON_SHOW = By.CLASS_NAME, "//div[@class='input__icon.input__icon-action']"
    PARENT_OBJECT = By.XPATH, "./.."
