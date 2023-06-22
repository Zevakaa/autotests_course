from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Переход на https://sbis.ru/
    driver.get("https://sbis.ru")
    sleep(2)

    # Переход в раздел "Контакты"
    header = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
    header.click()
    sleep(1)

    # Поиск баннера Тензор, клик по нему
    # Переход на https://tensor.ru/
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    banner.click()
    sleep(1)

    # Проверка что есть блок новости "Сила в людях"
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    sleep(1)
    news = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content " ".tensor_ru-Index__card-title")
    assert news.text == 'Сила в людях', 'Отсутствует блок с таким названием'
    driver.execute_script("return arguments[0].scrollIntoView(true);", news)
    sleep(2)

    # Переход в "Подробнее" с проверкой что открывается https://tensor.ru/about
    about = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    about.click()
    assert driver.current_url == 'https://tensor.ru/about', "Переход по неверной ссылке"
    sleep(2)


finally:
    driver.quit()
