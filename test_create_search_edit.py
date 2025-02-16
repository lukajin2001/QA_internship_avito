import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Путь к chromedriver
CHROMEDRIVER_PATH = "C:/Users/1/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe"

@pytest.fixture(scope="session", autouse=True)
def driver():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("http://tech-avito-intern.jumpingcrab.com/")
    
    yield driver
    
    driver.quit()


@pytest.mark.parametrize("name, price, description, image_url", [
    ("Тестовое объявление", "1000", "Описание объявления", "https://cdn2.iconfinder.com/data/icons/xomo-basics/128/document-03-1024.png")
])
def test_create_ad(driver, name, price, description, image_url):
    # Создание объявления
    driver.find_element(By.XPATH, "//button[text()='Создать']").click()
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "price").send_keys(price)
    driver.find_element(By.NAME, "description").send_keys(description)
    driver.find_element(By.NAME, "imageUrl").send_keys(image_url)
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(5)

    # Поиск объявления
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Поиск по объявлениям']")
    search_input.send_keys(name)
    driver.find_element(By.XPATH, "//button[text()='Найти']").click()
    driver.find_element(By.ID, "menu-button-:r5:").click()
    driver.find_element(By.XPATH, "//button[text()='25']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, f"//img[@src='{image_url}']").click()
    time.sleep(5)
    assert all(value in driver.page_source for value in [name, price, description, image_url]), "Не все данные найдены!"

@pytest.mark.parametrize("new_name, new_price, new_description, new_image_url", [
    ("Тест", "900", "Отредактирован", "https://avatars.mds.yandex.net/i?id=742a91fcbbedb351a7598f81d2eb7259_l-12569575-images-thumbs&n=13")
])
def test_edit_ad(driver, new_name, new_price, new_description, new_image_url):
    # Редактирование объявления
    driver.find_element(By.CSS_SELECTOR, "svg[style='cursor: pointer;']").click()
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(new_name)
    driver.find_element(By.NAME, "price").clear()
    driver.find_element(By.NAME, "price").send_keys(new_price)
    driver.find_element(By.NAME, "description").clear()
    driver.find_element(By.NAME, "description").send_keys(new_description)
    driver.find_element(By.NAME, "imageUrl").clear()
    driver.find_element(By.NAME, "imageUrl").send_keys(new_image_url)
    driver.find_element(By.CSS_SELECTOR, "svg[style='cursor: pointer;']").click()
    time.sleep(5)
    assert all(value in driver.page_source for value in [new_name, new_price, new_description]), "Не все данные найдены!"
    image_element = driver.find_element(By.XPATH, f"//img[@src='{new_image_url}']")
    assert image_element is not None 
