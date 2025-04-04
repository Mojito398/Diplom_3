from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    # Карточка заказа в истории заказов
    order_card = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    # Заголовок карточки заказа с названием бургера
    order_card_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    # Номер заказа в карточке заказа
    order_card_id = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits-default")])[1]')