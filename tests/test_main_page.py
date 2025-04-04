from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from conftest import *
import allure


class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_successful_navigation_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_header_feed_button()
        main_page.click_on_button_constructor()
        assert 'Соберите бургер' in main_page.get_text_on_title_of_constructor()

    @allure.title('Проверка перехода по клику на "Ленту заказов"')
    def test_successful_navigation_to_order_history(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'

    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_successful_display_of_modal_window_for_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.check_displaying_of_modal_details()

    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    def test_successful_closing_of_modal_window_for_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_modal()
        assert main_page.check_not_displaying_of_modal_details()

    @allure.title('Проверка увеличения числа на счетчике при добавлении ингредиента в заказ')
    def test_successful_counter_update_for_ingredients_in_order(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_order()
        assert main_page.get_count_of_ingredients() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_successful_order_creation_by_authenticated_user(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        main_page.click_on_button_login_in_main()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        assert main_page.check_displaying_of_confirmation_modal_of_order()