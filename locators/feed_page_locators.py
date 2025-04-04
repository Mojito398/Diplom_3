from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Раздел заказов
    section_orders_list = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    title_of_orders_feed = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Карточка заказа в ленте
    order_in_feed = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Всплывающее окно с деталями заказа
    modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]')

    # Заголовок всплывающего окна с деталями заказа
    title_of_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]//h2')

    # Счетчик заказов "Выполнено за все время"
    quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик заказов "Выполнено за сегодня"
    daily_quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Заказ в разделе "В работе"
    order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Номер заказа в разделе "В работе"
    number_of_order_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class,"text_type_digits-default")]')

    # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
    id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')