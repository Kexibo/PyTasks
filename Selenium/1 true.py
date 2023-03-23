"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
import json
import time



steam_data = {}
list_games = ['стратегии', 'шутеры', 'головоломки', 'приключения', 'экшен']

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://store.steampowered.com/search/?supportedlang=russian&ndl=1')

for j in list_games:
    s_search = driver.find_element(by='id', value = "term")
    s_search.clear()
    s_search.send_keys(j)
    s_search.send_keys(Keys.ENTER)
    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    container = soup.find('div', 'search_results')
    names = container.find_all('span', 'title')
    steam_data[j] = {}
    for i in range(len(names)):
        game_name = names[i].text.strip()
        steam_data[j][i+1] = ({'Игра' : game_name})

with open('steam.json', 'w', encoding="utf-8") as f:
    json.dump(steam_data, f, indent=4, ensure_ascii=False)