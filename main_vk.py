import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle


def login_vk():
    # write executable_path to driver, open max.size window & sleep
    driver = webdriver.Chrome(
        executable_path='/home/heyartem/PycharmProjects/Parsing_project/2021.07_tovary-dlya-doma/web_driver/chromedriver')
    try:
        # driver.maximize_window()
        #
        # # write url for driver, open window & sleep
        # driver.get(url='https://vk.com/')
        # time.sleep(5)
        #
        # email = driver.find_element_by_id('index_email')
        # email.clear()
        # email.send_keys('artem_white@mail.ru')
        # time.sleep(2)
        #
        # password = driver.find_element_by_id('index_pass')
        # password.clear()
        # password.send_keys('*1234ArtVK*')
        #
        # # driver.find_element_by_id('index_pass').clear()
        # # driver.find_element_by_id('index_pass').send_keys("password")
        #
        # time.sleep(2)
        #
        # # вариант имитация клика мышкой
        # # button = driver.find_element_by_id('index_login_button')
        # # button.click()
        #
        # # нажимаю на кнопку в одну строку
        # # driver.find_element_by_id('index_login_button').click()
        #
        # # вариант нажатие кнопки enter
        # password.send_keys(Keys.ENTER)
        # time.sleep(7)
        #
        # # save cookies
        # pickle.dump(driver.get_cookies(), open('art_vk_cookies', 'wb'))
        # time.sleep(5)

        driver.maximize_window()
        driver.get(url='https://vk.com/')
        time.sleep(5)

        # подгружаю куки в цикле
        for cookie in pickle.load(open('art_vk_cookies', 'rb')):
            driver.add_cookie(cookie)

        time.sleep(3)

        # обновление
        driver.refresh()
        time.sleep(10)

        "vk.com" "vk.c0m"

        "li"


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    login_vk()


if __name__ == '__main__':
    main()
