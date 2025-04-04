import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from helpers import *
import requests
from urls import Urls
import allure

# Функция для создания драйвера Chrome
def create_chrome_driver():
    options = Options()
    options.add_argument('--incognito')  # Открытие в режиме инкогнито
    driver = webdriver.Chrome(options=options)  # Создаем экземпляр драйвера
    driver.maximize_window()  # Открываем окно в полноэкранном режиме
    return driver

# Функция для создания драйвера Firefox
def create_firefox_driver():
    options = webdriver.FirefoxOptions()
    profile = FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    options.profile = profile
    driver = webdriver.Firefox(options=options)  # Создаем экземпляр драйвера
    driver.maximize_window()  # Открываем окно в полноэкранном режиме
    return driver

@pytest.fixture(params=[create_firefox_driver, create_chrome_driver], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    try:
        driver = request.param()  # Создаем драйвер с помощью выбранной функции
        driver.get(Urls.base_url)  # Открываем базовый URL
        yield driver  # Возвращаем драйвер для использования в тестах
    except Exception as e:
        pytest.fail(f"Failed to initialize the driver: {e}")
    finally:
        driver.quit()

#Фикстура генерирует случайные учетные данные пользователя
@pytest.fixture
def generate_user_credentials():
    email = create_random_email()
    password = create_random_password()
    name = create_random_name()
    return email, password, name


@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными кредами и удаляет его из базы после теста')
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(Urls.user_register, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Urls.user_delete, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ для его аккаунта')
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [
        '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
        '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79'
    ]}
    response_body = requests.post(Urls.order_create, data=payload, headers=headers)

    yield access_token, response_body
    requests.delete(Urls.user_delete, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура передает в драйвер токены созданного пользователя')
def set_user_tokens(driver, create_new_user_and_delete):
    driver.get(Urls.base_url)
    user_data = create_new_user_and_delete[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')