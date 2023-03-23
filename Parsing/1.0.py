
import lxml
from bs4 import BeautifulSoup
import time
import random
# import requests

# page = requests.get("https://krasnodar.technopark.ru/smartfony/")
# print(page)

import requests

cookies = {
    'stest201': '1',
    'stest207': 'acc0',
    'stest209': 'ct2',
    'PHPSESSID': '12355cec41496bac1287e71ec7cb3872',
    'user_public_id': 'CNa%2F%2F0pxwrS4W1lmKthfTeZauvzWNoj8jQ2C0weTk4Rj6Op8udBGZHPXDb0vCn%2Br',
    '_gcl_au': '1.1.180060429.1678789837',
    '_gid': 'GA1.2.1535651386.1678789837',
    '_ym_uid': '1678789837697367513',
    '_ym_d': '1678789837',
    'tmr_lvid': '15b0baf1ad77094c99be149549f88115',
    'tmr_lvidTS': '1678789837012',
    '_ym_visorc': 'b',
    '_ym_isad': '1',
    'afUserId': 'fc5d44ac-8bf1-4b2d-ac6d-149f3e5cfeaa-p',
    'AF_SYNC': '1678789839040',
    'tp_city_id': '38612',
    '_userGUID': '0:lf844rhm:xInE2CKAffnCqpQAg2HLh415jpCs2QaP',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%2049aedc6de44e5dca3ee7%22}',
    'promo1000closed': 'true',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    '_gat_UA-25136986-1': '1',
    'qrator_jsid': '1678789835.305.VLCvbEgK5PqlfFRc-3gfree4kpcjhm5dg5cbsku9m9d0na6kt',
    'visitedPagesNumber': '14',
    'tmr_detect': '1%7C1678794017377',
    '_ga_RD4H4CBNJ3': 'GS1.1.1678789836.1.1.1678794017.34.0.0',
    '_ga': 'GA1.2.2137600647.1678789837',
    'mindboxDeviceUUID': 'd81c5c61-bd89-4448-9589-578e635f67d7',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d81c5c61-bd89-4448-9589-578e635f67d7%22%7D',
    'pageviewTimer': '4315.732',
}

headers = {
    'authority': 'krasnodar.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'stest201=1; stest207=acc0; stest209=ct2; PHPSESSID=12355cec41496bac1287e71ec7cb3872; user_public_id=CNa%2F%2F0pxwrS4W1lmKthfTeZauvzWNoj8jQ2C0weTk4Rj6Op8udBGZHPXDb0vCn%2Br; _gcl_au=1.1.180060429.1678789837; _gid=GA1.2.1535651386.1678789837; _ym_uid=1678789837697367513; _ym_d=1678789837; tmr_lvid=15b0baf1ad77094c99be149549f88115; tmr_lvidTS=1678789837012; _ym_visorc=b; _ym_isad=1; afUserId=fc5d44ac-8bf1-4b2d-ac6d-149f3e5cfeaa-p; AF_SYNC=1678789839040; tp_city_id=38612; _userGUID=0:lf844rhm:xInE2CKAffnCqpQAg2HLh415jpCs2QaP; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%2049aedc6de44e5dca3ee7%22}; promo1000closed=true; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; _gat_UA-25136986-1=1; qrator_jsid=1678789835.305.VLCvbEgK5PqlfFRc-3gfree4kpcjhm5dg5cbsku9m9d0na6kt; visitedPagesNumber=14; tmr_detect=1%7C1678794017377; _ga_RD4H4CBNJ3=GS1.1.1678789836.1.1.1678794017.34.0.0; _ga=GA1.2.2137600647.1678789837; mindboxDeviceUUID=d81c5c61-bd89-4448-9589-578e635f67d7; directCrm-session=%7B%22deviceGuid%22%3A%22d81c5c61-bd89-4448-9589-578e635f67d7%22%7D; pageviewTimer=4315.732',
    'referer': 'https://krasnodar.technopark.ru/smartfony/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}


for i in range(1, 11):
    time.sleep(random.randint(1,5))
    response = requests.get(f'https://krasnodar.technopark.ru/smartfony/', params={'p':str(i)}, cookies=cookies, headers=headers)
    print(response, i)

# with open('page.html', 'w', encoding="utf-8") as f:
#     f.write(response.text)


# with open('page.html', 'r', encoding="utf-8") as f:
#     soup = BeautifulSoup(f.read(), 'lxml')
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find_all("div", "product-card-big__container")
    for i in container:
        name = i.find("div", "product-card-big__name").text[13:-11]
        price = i.find("div", "product-prices__price").text[5:-5]
        print('Название:', name, '\nЦена:',price)