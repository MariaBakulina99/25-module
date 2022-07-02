import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/Users/Maria/PycharmProjects/chromedriver')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mary.bakulina99@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Aws12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_all_pets_is_presented():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mary.bakulina99@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Aws12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку, чтобы открыть страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Сохраняем в переменную  элементы статистики
    statistics = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")
    # Получаем количество питомцев из данных статистики
    number = statistics[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # Находим питомцев на странице
    pets = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
    # сравниваем количество питомцев на странице с данными статистики
    for i in range(len(pets)):
        assert len(pets) == number


def test_half_of_pets_have_photo():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mary.bakulina99@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Aws12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку, чтобы открыть страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Задаем время неявного ожидания
    pytest.driver.implicitly_wait(6)
    # Находим все фото питомцев
    images = pytest.driver.find_elements_by_css_selector('th > img')
    # Проверяем загружена ли фотография и считаем питомцев, у которых она загружена
    count = 0
    for i in range(len(images)):
        if images[i].get_attribute('src'):
            count += 1
    assert count >= (len(images) / 2)


def test_all_pets_have_name_age_breed():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mary.bakulina99@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Aws12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку, чтобы открыть страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Задаем время неявного ожидания
    pytest.driver.implicitly_wait(4)
    # Находим питомцев на странице
    pets = pytest.driver.find_elements_by_css_selector('tbody > tr')
    # Находим все имена питомцев
    names = pytest.driver.find_elements_by_css_selector('tr > td:nth-child(2)')
    # Провяряем, что имя - это не пустой текст, и считаем у скольких питомцев оно есть
    count_names = 0
    for i in range(len(names)):
        if names[i].text != '':
            count_names += 1
    # Находим все породы питомцев
    breed = pytest.driver.find_elements_by_css_selector('tr > td:nth-child(3)')
    # Провяряем, что порода - это не пустой текст и считаем у скольких питомцев она есть
    count_breed = 0
    for i in range(len(breed)):
        if names[i].text != '':
            count_breed += 1
    # Находим возраст каждого питомца
    age = pytest.driver.find_elements_by_css_selector('tr > td:nth-child(4)')
    # Провяряем, что возраст - это не пустой текст и считаем у скольких питомцев он есть
    count_age = 0
    for i in range(len(age)):
        if names[i].text != '':
            count_age += 1
    for i in range(len(pets)):
    # Проверятем, что у всех питомцев есть имя, порода и возраст
        assert len(pets) == count_names and len(pets) == count_breed and len(pets) == count_age


def test_all_pets_have_unique_names():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mary.bakulina99@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Aws12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку, чтобы открыть страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Задаем время неявного ожидания
    pytest.driver.implicitly_wait(8)
    # Находим все имена питомцев
    names = pytest.driver.find_elements_by_css_selector('tr > td:nth-child(2)')
    # Сравниваем имена питомцев
    for i in range(len(names) - 1):
        for j in range(i + 1, len(names)):
            assert names[i].text != names[j].text


def test_all_pets_unique():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mary.bakulina99@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Aws12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку, чтобы открыть страницу "Мои питомцы"
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Находим всех питомцев
    pets = WebDriverWait(pytest.driver, 6).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tbody > tr')))
    # Сравниваем их между собой
    for i in range(len(pets)):
        for j in range(i + 1, len(pets)):
            assert pets[i].text != pets[j].text
