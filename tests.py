from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle


def loginToTwitch():
    """Данная функция собирает данные предпросмотра в поисковой строке сайта Twich, и все ссылки со страницы
    результатов поиска по тексту запроса из переменной search_request"""
    search_request = 'pool'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("mute-audio")
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.twitch.tv/login")
    for cookie in pickle.load(open('twich_cookies', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(3)
    driver.refresh()
    element = driver.find_element_by_tag_name("input")
    element.send_keys(search_request)
    elements = driver.find_elements_by_id("search-tray__container")
    time.sleep(3)
    for el in elements:
        print(f'Результаты предпросмотра в поиске по запросу {search_request}:\n {el.text}')
    element.send_keys(Keys.ENTER)
    time.sleep(3)
    elements = driver.find_elements_by_xpath("//a[@href]")
    time.sleep(5)
    print('\n', f'Все ссылки со страницы https://www.twitch.tv/search?term=pool: ')
    for el in elements:
        print(el.get_attribute("href"))
    driver.close()


if __name__ == '__main__':
    loginToTwitch()
