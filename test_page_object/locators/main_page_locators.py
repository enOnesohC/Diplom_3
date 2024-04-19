from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_CABINET = By.XPATH, "//p[text()='Личный Кабинет']"
    FEED_TEXT = By.XPATH, "//p[text()='Лента Заказов']"
    CONSTRUCTOR_TEXT = By.XPATH, "//p[text()='Конструктор']"
    BUTTON_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    OBJECT_ORDER = By.XPATH, "//p[text()='Соус Spicy-X']"
    BASE_ORDER = By.XPATH, "//li[contains(.,'Перетяните булочку сюда (верх)')]"
    WINDOW_OBJECT = By.XPATH, "//h2[text()='Детали ингредиента']"
    WINDOW_BUTTON_CLASS = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    SECTION_CLASS = By.XPATH, "//section[@class = 'Modal_modal__P3_V5']"
    TOTAL_PRICE = By.XPATH, "//p[@class = 'text text_type_digits-medium mr-3']"
    ORDER_NUMBER = By.XPATH, "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    BUTTON_CLOSE_ORDER_NUMBER = By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"