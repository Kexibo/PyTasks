"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import lxml
import json
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://class.sirius.ru/authorize')

s_search = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input')
s_search.clear()
s_search.send_keys('kexibo')

s_search = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input')
s_search.clear()
s_search.send_keys('767574737271Vit')

s_search.send_keys(Keys.ENTER)
time.sleep(1)
s_search = driver.find_element(By.XPATH, '/html/body/div[1]/div/header/div/div/div/nav/div/a[4]')
s_search.click()
time.sleep(1)

class_data = {}

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
container = soup.find_all('div', 'schedule__day')

for i in container:
    class_data[i.find("div", "column-40").text.strip()] = {}
    lessons = i.find_all("span", "schedule-lesson")
    
    for j in range(len(lessons)):
        class_data[i.find("div", "column-40").text.strip()][j+1] = lessons[j].text.strip()

with open('class.json', 'w', encoding="utf-8") as f:
    json.dump(class_data, f, indent=4, ensure_ascii=False)