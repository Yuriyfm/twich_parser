from selenium import webdriver
import pickle
from auth_data import login, password


def pause():
    input(
        'Введите в браузере вебдрайвера код подтверждения отправленный на вашу почту и пройдите капчу если она есть.'
        '\nЭто нужно для сохранения cookies. Вернитесь в скрипт и нажмите в консоли ENTER')


def FirstloginToTwitch():
    """Данная функция нужна для первого запуска Twich и сохранения данных cookies в файл 'twich_cookies'.
    Для последующих запусков используйте файл tests.py"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.twitch.tv/login")
    elem = driver.find_element_by_id("login-username")
    elem.send_keys(login)
    elem = driver.find_element_by_id('password-input')
    elem.submit()
    elem.send_keys(password)
    driver.implicitly_wait(10)
    elem = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button/div/div')
    elem.click()
    pause()
    pickle.dump(driver.get_cookies(), open('twich_cookies', 'wb'))
    driver.close()


if __name__ == '__main__':
    FirstloginToTwitch()
