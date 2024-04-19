from selenium.webdriver.common.by import By


class FeedPageLocators:
    TOTAL_COUNT_ORDER = By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    DAY_COUNT_ORDER = By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]"
    ORDERS_1 = By.XPATH, "(//div[@class = 'OrderHistory_textBox__3lgbs mb-6'])[1]"
    ORDERS_1_NUMBER = By.XPATH, "//p[@class = 'text text_type_digits-default mb-10 mt-5']"
    CURRENT_ORDER = By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']"
