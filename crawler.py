from selenium import webdriver
import time
import pickle

def init_browser(url):
    options = webdriver.ChromeOptions()
    options_list = ['disable-gpu', '--start-maximized', 'log-level=3']
    for opt in options_list:
        options.add_argument(opt)
    driver = r"assets\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=driver, options=options)
    browser.get(url)
    time.sleep(5)

    return browser


def parse_regs(html):
    css = 'div.col-md-12.data'
    try:
        reg_list = html.find_elements_by_css_selector(css)
    except:
        print('Problema na identicação dos registros')
    finally:
        return reg_list

def parse_fields(html):
    empresa_css = 'div.col-md-6 > a'
    local_css = 'div.col-md-4'
    receita_css = 'div.col-md-2.last'
    
    return {
        'empresa_nome': html.find_element_by_css_selector(empresa_css).text,
        'empresa_href': html.find_element_by_css_selector(empresa_css).get_attribute("href"),
        'local': html.find_element_by_css_selector(local_css).text,
        'receita': html.find_element_by_css_selector(receita_css).text
    }
    
    
url_base = "https://www.dnb.com/business-directory/company-information.coffee-tea-manufacturing.br.html?page="
pages_range = range(1, 21, 1)
url_list = [url_base + str(page) for page in pages_range]
wait = 5

parsed_regs = []
for page in pages_range:
    url = url_base + str(page)
    print(f'Começando a extrair os dados da página n.{page}')
    browser = init_browser(url)
    try:
        html_regs = parse_regs(browser)
        page_regs = [parse_fields(reg) for reg in html_regs]

        parsed_regs += page_regs
        print(len(parsed_regs)) 
    except:
        print('Erro')
    finally:
        browser.close()

with open(r"data\test_scrap.pickle", "wb") as file:
    pickle.dump(parsed_regs, file)