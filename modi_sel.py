import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


def a():
    try:
        # write executable_path to driver, open max.size window & sleep
        driver = webdriver.Chrome(
            executable_path='/home/heyartem/PycharmProjects/Parsing_project/2021.07_tovary-dlya-doma/web_driver/chromedriver')

        driver.get(url='https://www.modi.ru/catalog/tovary-dlya-doma/?set_filter=Y&filter_P1_MIN=&filter_P1_MAX=&sort=activefrom_desc&filter_181_MIN=&filter_95_2645610321=N&filter_95_2871910706=N&filter_95_841265288=N&filter_95_1159954462=N&filter_95_3678868925=N&filter_95_2889884971=N&filter_95_894006417=N&filter_95_3308380389=N&filter_95_2989936755=N&filter_95_725582281=N&filter_95_3260818684=N&filter_95_3421137111=N&filter_95_3169671233=N&filter_95_3994858278=N&filter_95_2568717232=N&filter_95_1233418=N&filter_95_1997922972=N&filter_95_1686742952=N&filter_95_328111934=N&filter_95_2201062063=N&filter_95_4097227321=N&filter_95_2498835420=N&filter_95_3824550730=N&filter_95_3955125592=N&filter_95_523233627=N&filter_95_1747507661=N&filter_95_518882156=N&filter_95_1776989178=N&filter_95_3225011138=N&filter_95_3176019847=N&filter_95_873309050=N&filter_95_4027270031=N&filter_95_1793239710=N&filter_95_4102438717=N&filter_95_1561856625=N&filter_95_706689767=N&filter_95_3004590941=N&filter_95_3289471947=N&filter_95_927051422=N&filter_95_809328642=N&filter_95_1195004052=N&filter_95_3936590966=N&filter_95_2321814931=N&filter_95_1900364053=N&filter_95_1471453794=N&filter_95_325927977=N&filter_95_1844435453=N&filter_95_1939418277=N&filter_95_2550111204=N&filter_95_3774393202=N&filter_95_1961208822=N&filter_95_3991730764=N&filter_95_76504953=N&filter_95_67021611=N&filter_95_820625382=N&page_count=128')
        driver.maximize_window()
        # time.sleep(7)
        #
        # phone = driver.find_element_by_class_name("header-top__phone-link")
        # time.sleep(2)
        # phone.click()
        # time.sleep(3)

        check_phone = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'header-top__phone-link')))
        phone = driver.find_element_by_class_name("header-top__phone-link").click()
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    a()


if __name__ == '__main__':
    main()
