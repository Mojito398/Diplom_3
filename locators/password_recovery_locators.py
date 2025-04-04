from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Кнопка "Восстановить пароль" на экране входа
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Поле ввода email
    input_email = (By.CLASS_NAME, 'input__textfield')

    # Кнопка "Восстановить" на странице ввода email
    button_recover = (By.CLASS_NAME, 'button_button__33qZ0')

    # Поле ввода пароля
    input_password = (By.CSS_SELECTOR, '.input_type_password .input__textfield')

    # Иконка, скрывающая (боль) пароль
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Пароль со статусом видимости
    value_password_is_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class,"input_status_active")]')
    # Пароль скрыт
    value_password_is_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class,"input_type_password")]')