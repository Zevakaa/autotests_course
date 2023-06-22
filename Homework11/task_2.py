from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
recipient_login, recipient_password = 'securitytest00', 'securitytest00securitytest00'
recipient = 'Фамилиёё Имечко Иванович'
message_text = 'Задание 2 - проверка отправки сообщения себе с последующим удалением'

try:
    # Авторизоваться на https://fix-online.sbis.ru/
    driver.get("https://fix-online.sbis.ru/")
    sleep(2)
    driver.find_element(By.NAME, 'Login').send_keys(recipient_login, Keys.ENTER)
    driver.find_element(By.NAME, 'Password').send_keys(recipient_password, Keys.ENTER)
    sleep(2)

    # Перейти в реестр Контакты
    driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle').click()
    sleep(2)

    # Отправить сообщение самому себе
    driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'controls-Search__nativeField_caretEmpty').send_keys(recipient, Keys.ENTER)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph').send_keys(message_text)
    driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow').click()
    sleep(2)

    # Убедиться, что сообщение появилось в реестре
    message = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert message.text == message_text, 'Не удалось найти сообщение'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.context_click(message)
    action_chains.perform()
    sleep(2)

    # Удалить это сообщение и убедиться, что удалили
    driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]').click()
    sleep(1)
    assert driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner') != message, 'Сообщение не удалено!'
    sleep(2)

finally:
    driver.quit()
