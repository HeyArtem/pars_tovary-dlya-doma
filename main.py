import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
import csv
import json
import random


# собираю данные с сайта www.modi.ru (товары для дома).Главная ошибка, я не писал кукис и парамс

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
        time.sleep(random.randrange(3, 6))
        # time.sleep(4)
        try:
            driver = webdriver.Chrome(executable_path='/home/heyartem/PycharmProjects/Parsing_project/2021.07_tovary-dlya-doma/web_driver/chromedriver')
            driver.maximize_window()
            time.sleep(4)

            # write url for driver, open window & sleep
            driver.get(url=pagination_page_url)
            time.sleep(random.randrange(8, 12))

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


# пишу реквесты по новой, т.к. первый раз я пренебрег кукисами и парамсaми
def get_data_2():

    cookies = {
        'referer_url': 'https%3A%2F%2Fwww.google.com%2F',
        '_ga': 'GA1.1.993144639.1625909533',
        '_ym_uid': '1625909534423423834',
        '_ym_d': '1625909534',
        '_fbp': 'fb.1.1625909533577.1030615383',
        'BX_USER_ID': '36bdc6039233d579cd830d06ad4cdce1',
        'user_unic_ac_id': '2dfb930a-63df-6a86-6258-099654ed3929',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'ada822e3-48bf-4b15-b869-7d479c8ae01c',
        'BITRIX_SM_SALE_UID': '83c155a14336018babba1019f2c69328',
        'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A14%2C%22EXPIRE%22%3A1626037140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
        '_ym_isad': '1',
        'PHPSESSID': '9eecb28487d2a406d707c4ca7858ec6e',
        '_ym_visorc': 'w',
        '_ga_X1XS85TFFB': 'GS1.1.1626011015.8.0.1626011015.0',
        'advcake_session': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
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

    r = requests.get('https://www.modi.ru/catalog/tovary-dlya-doma/', headers=headers, params=params)

    # create directory
    if not os.path.exists('data_tovary'):
        os.mkdir('data_tovary')

    # write to directory
    with open('data_tovary/index_tovary.html', 'w') as file:
        file.write(r.text)

    # read file
    with open('data_tovary/index_tovary.html') as file:
        src = file.read()

    # create object BeautifulSoup
    soup = BeautifulSoup(src, 'lxml')

    # looking for the last page
    last_page = int(soup.find('div', class_='pagination__list').find_all('div', class_='pagination__item')[-2].text.replace('\n', ''))
    # print(f'last page: {last_page}')

    # create variable for data json
    all_data_cards = []

    # create template for data csv
    with open('data_tovary/all_data_cards.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Name',
                'Current price',
                'Link'
            )
        )

    # requests for every page
    for pagination_page_count in range(1, last_page + 1):
        pagination_page_url = f'https://www.modi.ru/catalog/tovary-dlya-doma/?set_filter=Y&filter_P1_MIN=&filter_P1_MAX=&sort=activefrom_desc&filter_181_MIN=&filter_95_2645610321=N&filter_95_2871910706=N&filter_95_841265288=N&filter_95_1159954462=N&filter_95_3678868925=N&filter_95_2889884971=N&filter_95_894006417=N&filter_95_3308380389=N&filter_95_2989936755=N&filter_95_725582281=N&filter_95_3260818684=N&filter_95_3421137111=N&filter_95_3169671233=N&filter_95_3994858278=N&filter_95_2568717232=N&filter_95_1233418=N&filter_95_1997922972=N&filter_95_1686742952=N&filter_95_328111934=N&filter_95_2201062063=N&filter_95_4097227321=N&filter_95_2498835420=N&filter_95_3824550730=N&filter_95_3955125592=N&filter_95_523233627=N&filter_95_1747507661=N&filter_95_518882156=N&filter_95_1776989178=N&filter_95_3225011138=N&filter_95_3176019847=N&filter_95_873309050=N&filter_95_4027270031=N&filter_95_1793239710=N&filter_95_4102438717=N&filter_95_1561856625=N&filter_95_706689767=N&filter_95_3004590941=N&filter_95_3289471947=N&filter_95_927051422=N&filter_95_809328642=N&filter_95_1195004052=N&filter_95_3936590966=N&filter_95_2321814931=N&filter_95_1900364053=N&filter_95_1471453794=N&filter_95_325927977=N&filter_95_1844435453=N&filter_95_1939418277=N&filter_95_2550111204=N&filter_95_3774393202=N&filter_95_1961208822=N&filter_95_3991730764=N&filter_95_76504953=N&filter_95_67021611=N&filter_95_820625382=N&page_count=128&PAGEN_1={pagination_page_count}'

        r = requests.get(url=pagination_page_url)

        # save every page
        with open(f'data_tovary/pagination_page_{pagination_page_count}.html', 'w') as file:
            file.write(r.text)

        # read every page
        with open(f'data_tovary/pagination_page_{pagination_page_count}.html') as file:
            src = file.read()

        # create object BeautifulSoup
        soup = BeautifulSoup(src, 'lxml')

        # find block with cards
        all_cards = soup.find('div', class_='products-small__list').find_all('div', class_='products-small__item')

        for card in all_cards:

            try:
                # find name card
                card_name = card.find(class_='product-small__title-link').text
            except Exception as ex:
                print(ex)
                card_name = 'No data'

            try:
                # price current
                # card_price_current = card.find('div', class_='price price_sale').text.replace('\n', '')[0:4].replace('Р', '')
                card_price_current = card.find('nobr', class_='price__current').text
            except Exception as ex:
                print(ex)
                card_price_current = 'No data'

            try:
                # price old
                card_old_price = card.find('nobr', class_='price__old').text
            except Exception as ex:
                card_old_price = 'No data'



            try:
                # link of card
                card_link = f"https://www.modi.ru/{card.find('div', class_='product-small__main-top').find('a', class_='link-image').get('href')}"
            except Exception as ex:
                print(ex)
                card_link = 'No data'

            # write data in csv
            with open('data_tovary/all_data_cards.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        card_name,
                        card_price_current,
                        card_link
                    )
                )

            # packing data in variable for json
            all_data_cards.append(
                {
                    'card_name': card_name,
                    'card_price_current': card_price_current,
                    'card_link': card_link
                }
            )

            print(f'Наименование: {card_name}\nТекущая цена: {card_price_current}\nСсылка на карточку: {card_link}\nСтарая цена: {card_old_price}\n')

        # monitor of progress
        print(f'--> {pagination_page_count} of {last_page}')
        time.sleep(random.randrange(3, 6))

    # write data in json
    with open('data_tovary/all_data_cards.json', 'a') as file:
        json.dump(all_data_cards, file, indent=4, ensure_ascii=False)


def main():
    get_data_2()
    # get_data_selenium()


if __name__ == '__main__':
    main()
