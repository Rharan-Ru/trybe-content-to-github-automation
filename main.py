from main_functions.login import login
from main_functions.get_exe_data import main_script
from main_functions.timer import timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

print('Selecione o conteúdo: ')
print('0 - Fundamentals')
print('1 - Frontend')
print('2 - Backend')
print('3 - Computer Science')

list_sites = ['fundamentals', 'front-end', 'backend', 'computer-science']
selected_site = int(input(': '))
SITE_URL = f'https://app.betrybe.com/course/calendar/{list_sites[selected_site]}'

def main():
    service_obj = Service(executable_path="./drivers/geckodriver")
    browser = webdriver.Firefox(service=service_obj)
    browser.get(SITE_URL)
    timer(browser, 'NAME', 'email')
    try:
        login(browser)
    except Exception as error:
        print(error)
        browser.quit()
    try:
        timer(browser, "CLASS_NAME", "module-index-content")
    except Exception as error:
        print(error)
        browser.get(SITE_URL)
        timer(browser, "CLASS_NAME", "module-index-content")
    keys = browser.find_elements(By.CLASS_NAME, "ada-accordion")
    main_script(browser, keys, SITE_URL)
    print('MAPEAMENTO COMPLETO')
    browser.quit()

main()
