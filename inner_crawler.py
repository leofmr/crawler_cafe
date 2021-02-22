from selenium import webdriver
import time
import pickle

def load_hrefs(file_path=r'data\test_scrap.pickle', href_loc='empresa_href'):
    with open(file_path, "rb") as file:
        regs_data = pickle.load(file)

    return [reg[href_loc] for reg in regs_data]


def empresa_parser(link, wait=5, driver = r"assets\chromedriver.exe"):

    options = webdriver.ChromeOptions()    
    browser = webdriver.Chrome(executable_path=driver, options=options)
    browser.get(link)
    time.sleep(5)

    # descricao_css = 'span.company_summary'
    industria_css = 'span.profile-industry-item'
    website_css = 'a#hero-company-link.ext-icon'
    # contato_css = 'div.profile_see_more_col > span'

    # descricao_xpath = '//*[@id="content"]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/div/span'
    # contato_xpath = '//*[@id="content"]/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/div/span[1]'

    data = {}
    data['url'] = link
    try:
        data['website'] = browser.find_element_by_css_selector(website_css).get_attribute('href')
    except:
        data['website'] = None
    
    try:
        data['descricao'] = browser.find_element_by_class_name('company_summary').get_attribute('outerHTML')
    except:
        data['descricao'] = None

    try:
        data['industria'] = [el.text for el in browser.find_elements_by_css_selector(industria_css)]
    except:
        data['industria'] = None
    
    browser.close()
    return data


url_list = load_hrefs()
results = [empresa_parser(url) for url in url_list]
with open(r"data\inner_scrap.pickle", "wb") as file:
    pickle.dump(results, file)