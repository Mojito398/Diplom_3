from page_objects.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from helpers import *
import allure


class PasswdRecoveryPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def navigate_to_recovery_passwd_page(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.button_forgot_password)
        self.click_on_element(PasswordRecoveryLocators.button_forgot_password)

    @allure.step('Проверить отображение поля email')
    def check_displaying_of_input_email(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.input_email)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.input_email)
        email = create_random_email()
        self.send_keys_to_input(PasswordRecoveryLocators.input_email, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.button_recover)
        self.click_on_element(PasswordRecoveryLocators.button_recover)

    @allure.step('Проверить отображение поля password')
    def check_displaying_of_input_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.input_password)
        return self.check_displaying_of_element(PasswordRecoveryLocators.input_password)

    @allure.step('Ввести password')
    def send_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.input_password)
        passwd = create_random_password()
        self.send_keys_to_input(PasswordRecoveryLocators.input_password, passwd)

    @allure.step('Кликнуть на иконку глаза в поле ввода пароля')
    def click_on_eye_icon(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.eye_icon)
        self.click_on_element(PasswordRecoveryLocators.eye_icon)

    @allure.step('Проверить, что значение поля password отображается')
    def check_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.value_password_is_visible)

    @allure.step('Проверить, что значение поля password не отображается')
    def check_not_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.value_password_is_invisible)