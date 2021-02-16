from selenium import webdriver
import time


def empresa_parser(link):
    browser = webdriver.Chrome(executable_path=driver, options=options)
    browser.get(link)
    time.sleep(5)

    descricao_css = 'span.company_summary'
    industria_css = 'span.profile-industry-item'
    website_css = 'a#hero-company-link.ext-icon'
    contato_css = 'div.profile_see_more_col > span'

    descricao_xpath = '//*[@id="content"]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/div/span'
    contato_xpath = '//*[@id="content"]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/div/span[1]'

    data = {}
    try:
        data = {
            'website': browser.find_element_by_css_selector(website_css).get_attribute('href'),
            'descricao': browser.find_element_by_class_name('company_summary').get_attribute('outerHTML'),
            # 'contato': browser.find_element_by_xpath(contato_xpath).text,
            'industria': [el.text for el in browser.find_elements_by_css_selector(industria_css)] 
        }
    finally:
        browser.close()
        return data


url1 = 'https://www.dnb.com/business-directory/company-profiles.tres_coracoes_alimentos_s-a.b2294d60d2c3f9c5f520b6db82fa0791.html'
url2 = 'https://www.dnb.com/business-directory/company-profiles.cafe_tres_coracoes_s-a.fb90ecf8e77b2932a813ac9e9d4774cf.html'
url3 = 'https://www.dnb.com/business-directory/company-profiles.cooperativa_dos_cafeicultores_da_zona_de_tres_pontas_ltda.640efe994e7297c9694b67b6004674ed.html'
url4 = 'https://www.dnb.com/business-directory/company-profiles.companhia_cacique_de_caf%C3%A9_sol%C3%BAvel.00372e6a2ba5c264f860c0705ae1caf8.html'

url_list = [url1, url2, url3, url4]
wait = 5
options = webdriver.ChromeOptions()
driver = r"assets\chromedriver.exe"


try:
    for url in url_list:
        print(empresa_parser(url))
        print()

finally:
    pass