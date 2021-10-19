import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import csv
import json
import random


# Этот код написал Макс и реквесты у него работаю, потому что у удалил cookies % params
# собираю данные с сайта www.modi.ru (товары для дома).
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'BX-CACHE-MODE': 'HTMLCACHE',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'BX-CACHE-BLOCKS': '{"LkGdQn":"df420eb6f80b","XEVOpk":"e89beeaceb20","iIjGFB":"bbadbd1feddd","CKtZPX":"0d6ce146f699","NMQc3w":"e89beeaceb20","oLJPsr":"658494d9c188","QCJ7Jg":"e4b6a12d94d0"}',
    'BX-REF': 'https://www.modi.ru/catalog/tovary-dlya-doma/?sort=activefrom_desc&filter_count=32&set_filter=Y&filter_P1_MIN=&filter_P1_MAX=&filter_181_MIN=&filter_95_2645610321=N&filter_95_2871910706=N&filter_95_841265288=N&filter_95_1159954462=N&filter_95_3678868925=N&filter_95_2889884971=N&filter_95_894006417=N&filter_95_3308380389=N&filter_95_2989936755=N&filter_95_725582281=N&filter_95_3260818684=N&filter_95_3421137111=N&filter_95_3169671233=N&filter_95_3994858278=N&filter_95_2568717232=N&filter_95_1233418=N&filter_95_1997922972=N&filter_95_1686742952=N&filter_95_328111934=N&filter_95_2201062063=N&filter_95_4097227321=N&filter_95_2498835420=N&filter_95_3824550730=N&filter_95_3955125592=N&filter_95_523233627=N&filter_95_1747507661=N&filter_95_518882156=N&filter_95_1776989178=N&filter_95_3225011138=N&filter_95_3176019847=N&filter_95_873309050=N&filter_95_4027270031=N&filter_95_1793239710=N&filter_95_4102438717=N&filter_95_1561856625=N&filter_95_706689767=N&filter_95_3004590941=N&filter_95_3289471947=N&filter_95_927051422=N&filter_95_809328642=N&filter_95_1195004052=N&filter_95_3936590966=N&filter_95_2321814931=N&filter_95_1900364053=N&filter_95_1471453794=N&filter_95_325927977=N&filter_95_1844435453=N&filter_95_1939418277=N&filter_95_2550111204=N&filter_95_3774393202=N&filter_95_1961208822=N&filter_95_3991730764=N&filter_95_76504953=N&filter_95_67021611=N&filter_95_820625382=N&page_count=128',
    'BX-ACTION-TYPE': 'get_dynamic',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.modi.ru/catalog/tovary-dlya-doma/',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}


# сайт товары для дома, не отдает инфу через рекчвест, поэтому использую selenium
def get_data_selenium():
    try:
        # write executable_path to driver, open max.size window & sleep
        driver = webdriver.Chrome(executable_path='/home/heyartem/PycharmProjects/Parsing_project/2021.07_tovary-dlya-doma/web_driver/chromedriver')
        driver.maximize_window()
        time.sleep(5)

        # write url for driver, open window & sleep
        driver.get(url='https://www.modi.ru/catalog/tovary-dlya-doma/?set_filter=Y&filter_P1_MIN=&filter_P1_MAX=&sort=activefrom_desc&filter_181_MIN=&filter_95_2645610321=N&filter_95_2871910706=N&filter_95_841265288=N&filter_95_1159954462=N&filter_95_3678868925=N&filter_95_2889884971=N&filter_95_894006417=N&filter_95_3308380389=N&filter_95_2989936755=N&filter_95_725582281=N&filter_95_3260818684=N&filter_95_3421137111=N&filter_95_3169671233=N&filter_95_3994858278=N&filter_95_2568717232=N&filter_95_1233418=N&filter_95_1997922972=N&filter_95_1686742952=N&filter_95_328111934=N&filter_95_2201062063=N&filter_95_4097227321=N&filter_95_2498835420=N&filter_95_3824550730=N&filter_95_3955125592=N&filter_95_523233627=N&filter_95_1747507661=N&filter_95_518882156=N&filter_95_1776989178=N&filter_95_3225011138=N&filter_95_3176019847=N&filter_95_873309050=N&filter_95_4027270031=N&filter_95_1793239710=N&filter_95_4102438717=N&filter_95_1561856625=N&filter_95_706689767=N&filter_95_3004590941=N&filter_95_3289471947=N&filter_95_927051422=N&filter_95_809328642=N&filter_95_1195004052=N&filter_95_3936590966=N&filter_95_2321814931=N&filter_95_1900364053=N&filter_95_1471453794=N&filter_95_325927977=N&filter_95_1844435453=N&filter_95_1939418277=N&filter_95_2550111204=N&filter_95_3774393202=N&filter_95_1961208822=N&filter_95_3991730764=N&filter_95_76504953=N&filter_95_67021611=N&filter_95_820625382=N&page_count=128')
        time.sleep(12)

        # check and create a directory
        if not os.path.exists('data_selenium'):
            os.mkdir('data_selenium')

        # save the page
        with open('data_selenium/index_tovary_selenium.html', 'w') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)

    # be sure to close the driver and exit
    finally:
        driver.close()
        driver.quit()

    # read file
    with open('data_selenium/index_tovary_selenium.html') as file:
            src = file.read()

    # creat object BeautifulSoup
    soup = BeautifulSoup(src, 'lxml')

    # looking for the last page
    last_page = soup.find('div', class_='pagination__list').find_all('div', class_='pagination__item')[-2].text.replace('\n', '')
    print(f'last page: {last_page}')

    # requests for every page
    for pagination_page_count in range (1, 4): #(1, last_page + 1)
        pagination_page_url = f'https://www.modi.ru/catalog/tovary-dlya-doma/?set_filter=Y&filter_P1_MIN=&filter_P1_MAX=&sort=activefrom_desc&filter_181_MIN=&filter_95_2645610321=N&filter_95_2871910706=N&filter_95_841265288=N&filter_95_1159954462=N&filter_95_3678868925=N&filter_95_2889884971=N&filter_95_894006417=N&filter_95_3308380389=N&filter_95_2989936755=N&filter_95_725582281=N&filter_95_3260818684=N&filter_95_3421137111=N&filter_95_3169671233=N&filter_95_3994858278=N&filter_95_2568717232=N&filter_95_1233418=N&filter_95_1997922972=N&filter_95_1686742952=N&filter_95_328111934=N&filter_95_2201062063=N&filter_95_4097227321=N&filter_95_2498835420=N&filter_95_3824550730=N&filter_95_3955125592=N&filter_95_523233627=N&filter_95_1747507661=N&filter_95_518882156=N&filter_95_1776989178=N&filter_95_3225011138=N&filter_95_3176019847=N&filter_95_873309050=N&filter_95_4027270031=N&filter_95_1793239710=N&filter_95_4102438717=N&filter_95_1561856625=N&filter_95_706689767=N&filter_95_3004590941=N&filter_95_3289471947=N&filter_95_927051422=N&filter_95_809328642=N&filter_95_1195004052=N&filter_95_3936590966=N&filter_95_2321814931=N&filter_95_1900364053=N&filter_95_1471453794=N&filter_95_325927977=N&filter_95_1844435453=N&filter_95_1939418277=N&filter_95_2550111204=N&filter_95_3774393202=N&filter_95_1961208822=N&filter_95_3991730764=N&filter_95_76504953=N&filter_95_67021611=N&filter_95_820625382=N&page_count=128&PAGEN_1={pagination_page_count}'

        # pause between requests
        # time.sleep(random.randrange(3, 6))
        time.sleep(4)
        try:
            driver = webdriver.Chrome(executable_path='/home/heyartem/PycharmProjects/Parsing_project/2021.07_tovary-dlya-doma/web_driver/chromedriver')
            driver.maximize_window()
            time.sleep(4)

            # write url for driver, open window & sleep
            driver.get(url=pagination_page_url)
            # time.sleep(random.random.randrange(8, 12))
            time.sleep(8)

            # save page
            with open(f'data_selenium/pagination_page_{pagination_page_count}.html', 'w') as file:
                file.write(driver.page_source)

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()

        # progress monitor
        print(f'--> finished page: {pagination_page_count}')


def get_data():
    r = requests.get('https://www.modi.ru/catalog/tovary-dlya-doma/?set_filter=Y&filter_P1_MIN=&filter_P1_MAX=&sort=activefrom_desc&filter_181_MIN=&filter_95_2645610321=N&filter_95_2871910706=N&filter_95_841265288=N&filter_95_1159954462=N&filter_95_3678868925=N&filter_95_2889884971=N&filter_95_894006417=N&filter_95_3308380389=N&filter_95_2989936755=N&filter_95_725582281=N&filter_95_3260818684=N&filter_95_3421137111=N&filter_95_3169671233=N&filter_95_3994858278=N&filter_95_2568717232=N&filter_95_1233418=N&filter_95_1997922972=N&filter_95_1686742952=N&filter_95_328111934=N&filter_95_2201062063=N&filter_95_4097227321=N&filter_95_2498835420=N&filter_95_3824550730=N&filter_95_3955125592=N&filter_95_523233627=N&filter_95_1747507661=N&filter_95_518882156=N&filter_95_1776989178=N&filter_95_3225011138=N&filter_95_3176019847=N&filter_95_873309050=N&filter_95_4027270031=N&filter_95_1793239710=N&filter_95_4102438717=N&filter_95_1561856625=N&filter_95_706689767=N&filter_95_3004590941=N&filter_95_3289471947=N&filter_95_927051422=N&filter_95_809328642=N&filter_95_1195004052=N&filter_95_3936590966=N&filter_95_2321814931=N&filter_95_1900364053=N&filter_95_1471453794=N&filter_95_325927977=N&filter_95_1844435453=N&filter_95_1939418277=N&filter_95_2550111204=N&filter_95_3774393202=N&filter_95_1961208822=N&filter_95_3991730764=N&filter_95_76504953=N&filter_95_67021611=N&filter_95_820625382=N&page_count=128&PAGEN_1=15', headers=headers)

    # create directory
    if not os.path.exists('data_tovary'):
        os.mkdir('data_tovary')

    # write to directory
    with open('data_tovary/index_tovary.html', 'w') as file:
        file.write(r.text)

    # find the pagination block and the last page


def get_data2():
    import requests

    cookies = {
        'PHPSESSID': '0820404b4fbc2e2b63bf1808ac10c502',
        'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A14%2C%22EXPIRE%22%3A1626037140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
        '_ga_X1XS85TFFB': 'GS1.1.1625995261.1.0.1625995261.0',
        '_ga': 'GA1.1.853122506.1625995261',
        '_ym_uid': '1625995262359195899',
        '_ym_d': '1625995262',
        'user_unic_ac_id': 'f71867d7-0a35-2677-1881-6ba25397c047',
        'advcake_session': '1',
        '_ym_isad': '1',
        'BX_USER_ID': 'c582f22e291f5ee7dd919bf871be9a1e',
        '_ym_visorc': 'w',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'f1ce035b-1b29-459d-9ca9-eba296f3f5a8',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en,ru;q=0.9,ru-RU;q=0.8,en-US;q=0.7',
    }

    params = (
        ('set_filter', 'Y'),
        ('filter_P1_MIN', ''),
        ('filter_P1_MAX', ''),
        ('sort', 'activefrom_desc'),
        ('filter_181_MIN', ''),
        ('filter_95_2645610321', 'N'),
        ('filter_95_2871910706', 'N'),
        ('filter_95_841265288', 'N'),
        ('filter_95_1159954462', 'N'),
        ('filter_95_3678868925', 'N'),
        ('filter_95_2889884971', 'N'),
        ('filter_95_894006417', 'N'),
        ('filter_95_3308380389', 'N'),
        ('filter_95_2989936755', 'N'),
        ('filter_95_725582281', 'N'),
        ('filter_95_3260818684', 'N'),
        ('filter_95_3421137111', 'N'),
        ('filter_95_3169671233', 'N'),
        ('filter_95_3994858278', 'N'),
        ('filter_95_2568717232', 'N'),
        ('filter_95_1233418', 'N'),
        ('filter_95_1997922972', 'N'),
        ('filter_95_1686742952', 'N'),
        ('filter_95_328111934', 'N'),
        ('filter_95_2201062063', 'N'),
        ('filter_95_4097227321', 'N'),
        ('filter_95_2498835420', 'N'),
        ('filter_95_3824550730', 'N'),
        ('filter_95_3955125592', 'N'),
        ('filter_95_523233627', 'N'),
        ('filter_95_1747507661', 'N'),
        ('filter_95_518882156', 'N'),
        ('filter_95_1776989178', 'N'),
        ('filter_95_3225011138', 'N'),
        ('filter_95_3176019847', 'N'),
        ('filter_95_873309050', 'N'),
        ('filter_95_4027270031', 'N'),
        ('filter_95_1793239710', 'N'),
        ('filter_95_4102438717', 'N'),
        ('filter_95_1561856625', 'N'),
        ('filter_95_706689767', 'N'),
        ('filter_95_3004590941', 'N'),
        ('filter_95_3289471947', 'N'),
        ('filter_95_927051422', 'N'),
        ('filter_95_809328642', 'N'),
        ('filter_95_1195004052', 'N'),
        ('filter_95_3936590966', 'N'),
        ('filter_95_2321814931', 'N'),
        ('filter_95_1900364053', 'N'),
        ('filter_95_1471453794', 'N'),
        ('filter_95_325927977', 'N'),
        ('filter_95_1844435453', 'N'),
        ('filter_95_1939418277', 'N'),
        ('filter_95_2550111204', 'N'),
        ('filter_95_3774393202', 'N'),
        ('filter_95_1961208822', 'N'),
        ('filter_95_3991730764', 'N'),
        ('filter_95_76504953', 'N'),
        ('filter_95_67021611', 'N'),
        ('filter_95_820625382', 'N'),
        ('page_count', '128'),
        ('PAGEN_1', '15'),
    )

    response = requests.get('https://www.modi.ru/catalog/tovary-dlya-doma/', headers=headers, params=params,
                            cookies=cookies)

    if not os.path.exists('data_tovary'):
        os.mkdir('data_tovary')

    # write to directory
    with open('data_tovary/index_tovary.html', 'w') as file:
        file.write(response.text)


def main():
    # get_data()
    get_data2()
    # get_data_selenium()


if __name__ == '__main__':
    main()
