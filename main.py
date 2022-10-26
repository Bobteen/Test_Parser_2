from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

work = Session()
work.get('http://quotes.toscrape.com/', headers=headers)


