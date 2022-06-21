from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def timer(browser, attr, text, timeout=20):
    attr = attr.upper()
    if 'TAG' == attr:
        WebDriverWait(browser, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, text))
    elif 'CLASS_NAME' == attr:
        WebDriverWait(browser, timeout=timeout).until(lambda d: d.find_element(By.CLASS_NAME, text))
    elif 'NAME' == attr:
        WebDriverWait(browser, timeout=timeout).until(lambda d: d.find_element(By.NAME, text))