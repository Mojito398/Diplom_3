from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from page_objects.order_history_page import OrderHistoryPage
from conftest import *
import allure


class TestAccountPage:
    @allure.title('Проверка перехода в профиль по клику на "Личный кабинет" в хэдере')
    def test_successful_navigation_to_account_page(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        assert account_page.check_displaying_of_description() is True

    @allure.title('Проверка перехода по клику на «История заказов»')
    def test_successful_navigation_to_order_history_page(self, driver, set_user_tokens, create_user_and_order_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_on_order_history_button()
        order_history_page.wait_visibility_of_order_card()
        assert 'бургер' in order_history_page.get_text_of_order_card_title()

    @allure.title('Проверка выполнения логаута по кнопке "Выйти"')
    def test_successful_logout_from_profile_page(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_on_logout_button()
        account_page.wait_visibility_of_button_register()
        assert account_page.check_displaying_of_button_register()