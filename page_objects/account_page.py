from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure


class AccountPage(BasePage):
    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(AccountPageLocators.order_history)

    @allure.step('Кликнуть по кнопке "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(AccountPageLocators.button_logout)

    @allure.step('Подождать прогрузки текста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(AccountPageLocators.description_of_section)

    @allure.step('Проверить отображение описания раздела')
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(AccountPageLocators.description_of_section)

    @allure.step('Подождать прогрузки кнопки "Зарегистрироваться"')
    def wait_visibility_of_button_register(self):
        self.wait_visibility_of_element(AccountPageLocators.button_register)

    @allure.step('Проверить отображение кнопки "Зарегистрироваться"')
    def check_displaying_of_button_register(self):
        return self.check_displaying_of_element(AccountPageLocators.button_register)