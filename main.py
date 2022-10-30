from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}


def authorization():
    work = Session()

    work.get('http://quotes.toscrape.com/', headers=headers)  # вход на сайт

    responce = work.get('https://quotes.toscrape.com/login', headers=headers)  # вход на страничку с формой авторизации

    soup1 = BeautifulSoup(responce.text, 'lxml')

    token = soup1.find('form').find('input').get('value')  # забираем скрытый токен

    data = {'csrf_token': token, 'username': 'noname', 'password': 'password'}  # формируем словарь для заполнения формы
    return data


# def get_url(work):
#     result = work.post(f'https://quotes.toscrape.com/login/', headers=headers, data=data,
#                            allow_redirects=True)
#     soup2 = BeautifulSoup(result.text, 'lxml')
#
#
# list_card = soup2.find_all('div', class_='quote')
# text = soup2.find_all('span', class_='text')
