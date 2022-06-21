from selenium.webdriver.common.by import By
import getpass


def login(browser):
    email_box = browser.find_element(By.NAME, "email")
    password_box = browser.find_element(By.NAME, "password")
    email = input('Digite seu email: ')
    email_box.send_keys(email)
    password = getpass.getpass('Digite sua senha: ')
    password_box.send_keys(password)
    login_button = browser.find_element(By.CLASS_NAME, "c-kgnKGo")
    login_button.click()
