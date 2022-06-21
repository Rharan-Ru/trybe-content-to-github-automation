from main_functions.create_files import create_files
from main_functions.timer import timer
from selenium.webdriver.common.by import By

def create_readme(texto, path):
    with open(f'{path}/README.md', 'a') as fd:
        fd.write(f'{texto}\n\n')
        fd.close()


def clean_text(texto):
    return f'* {" ".join(texto.split())}'


def loop_divs(list_divs, path, btn_text):
    counter = 1
    create_readme(btn_text, path)
    print(btn_text)
    for exe in list_divs:
        text_new = clean_text(exe.get_attribute('textContent'))
        if '. ' in text_new[0:6] or '- ' in text_new[0:6]:
            # Escreve texto
            texto = f'{counter}. {text_new}'
            create_readme(texto, path)
            print(texto)
            counter += 1
            try:
                baixo = exe.find_element(By.XPATH, "./following-sibling::ol")
                baixo_li = baixo.find_elements(By.TAG_NAME, 'li')
                for li in baixo_li:
                    texto = clean_text(li.get_attribute('textContent'))
                    create_readme(texto, path)
                    print(texto)
            except Exception:
                try:
                    baixo = exe.find_element(
                        By.XPATH, "./following-sibling::ul")
                    baixo_li = baixo.find_elements(By.TAG_NAME, 'li')
                    for li in baixo_li:
                        texto = clean_text(li.get_attribute('textContent'))
                        create_readme(texto, path)
                        print(texto)
                except Exception:
                    continue


def loop_ol(list_li, path, btn_text):
    counter = 1
    create_readme(btn_text, path)
    print(btn_text)
    for ol in list_li:
        li_elements = ol.find_elements(By.CSS_SELECTOR, 'li')
        for exe in li_elements:
            texto = f'{counter}. {clean_text(exe.get_attribute("textContent"))}'
            create_readme(texto, path)
            print(texto)
            counter += 1
        try:
            baixo = ol.find_element(By.XPATH, "./following-sibling::ul")
            baixo_li = baixo.find_elements(By.TAG_NAME, 'li')
            for li in baixo_li:
                texto = clean_text(li.get_attribute('textContent'))
                create_readme(texto, path)
                print(texto)
        except Exception:
            continue


def get_exe_data(browser, element, path):
    browser.get(element.get_attribute('href'))
    timer(browser, 'CLASS_NAME', 'block-section')
    element_block = browser.find_element(By.CLASS_NAME, "block-section")
    buttons = element_block.find_elements(By.TAG_NAME, 'li')
    for btn in buttons:
        if 'exercicios' in btn.get_attribute('id'):
            btn_exercicio = btn.find_elements(By.TAG_NAME, 'button')[1:]
    for btn_exe in btn_exercicio:
        btn_text = f"## {btn_exe.get_attribute('textContent')}"
        btn_exe.click()
        timer(browser, 'CLASS_NAME', 'content-section-box')
        content = browser.find_element(By.CLASS_NAME, 'content-section-box')
        list_divs = content.find_elements(By.CSS_SELECTOR, 'div')
        list_ol = content.find_elements(By.CSS_SELECTOR, 'ol')
        if len(list_ol) > 0:
            loop_ol(list_ol, path, btn_text)
        else:
            loop_divs(list_divs, path, btn_text)


def main_script(browser, keys, path):
    actual_value = 0
    timer(browser, 'CLASS_NAME', 'ada-accordion')
    for primary_index in range(len(keys)):
        primary_element = browser.find_elements(By.CLASS_NAME, "ada-accordion")[primary_index]
        value = len(primary_element.find_elements(By.CLASS_NAME, "accordion-content-item")) + actual_value
        num_items = value - actual_value
        secondary_index = 1
        ele1_text = primary_element.text
        print(ele1_text.upper())
        for index_value in range(actual_value, value):
            secondary_element = browser.find_elements(By.CLASS_NAME, "accordion-content-item")[index_value]
            index = f'{primary_index+1}.{secondary_index}'
            ele2_text = secondary_element.get_attribute("textContent")
            print(ele2_text)
            child_path = create_files(ele1_text, ele2_text, index)

            if secondary_index == num_items: secondary_index = 1
            else: secondary_index += 1

            try:
                if 'projeto' in ele2_text.lower(): raise Exception('Não há exercicios em Projetos')
                get_exe_data(browser, secondary_element, child_path)
            except Exception:
                browser.get(path)
                timer(browser, 'CLASS_NAME', 'ada-accordion')
                continue
            browser.get(path)
            timer(browser, 'CLASS_NAME', 'ada-accordion')
        actual_value = value