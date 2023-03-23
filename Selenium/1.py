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
driver = webdriver.Chrome(options=options)

driver.get('https://store.steampowered.com/')
s_search = driver.find_element(by='id', value = "store_nav_search_term")
#s_search = driver.find_element_by_id("store_nav_search_term")
#s_search = driver.find_element(By.XPATH, '//*[@id="store_nav_search_term"]')

s_search.send_keys('стратегии')
s_search.send_keys(Keys.ENTER)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
container = soup.find('div', 'search_results')
names = container.find_all('span', 'title')
# results = {}
# k = 1
# for i in names:
#     results[i.text] = k
#     k+=1
# print(results)

# steam_data = []
# num = 0

# for name in names:
#     num += 1
#     steam_data.append({
#             '№': num,
#             'Игра': name.text,
#         })




for i in range(len(names)):
    game_name = names[i].text.strip()
    steam_data[i+1] = ({'Игра' : game_name})


with open('steam.json', 'w', encoding="utf-8") as f:
    json.dump(steam_data, f, indent=4, ensure_ascii=False)