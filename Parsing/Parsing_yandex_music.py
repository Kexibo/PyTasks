import lxml
from bs4 import BeautifulSoup
import time
import random
import requests
import json

cookies = {
    'yabs-frequency': '/5/G00049ZfsC00000/',
    'gdpr': '0',
    '_ym_uid': '1671914309300264081',
    '_ym_d': '1671914314',
    'yashr': '1345913691675985995',
    'is_gdpr': '0',
    'is_gdpr_b': 'CIG7UxDEqAEoAg==',
    '_ym_isad': '2',
    'i': 'ff1yL/JpgXDnoTSyqGgM6ZjxPrAqw3j4SM3giCYvEvP3nmZ2k6bSFbAvgpTAu25EYufeo9rJ9iLRoUBAOp2yh11Ftwk=',
    'yandexuid': '7277640731678798175',
    '_yasc': 'Lpj7B0xHIKUywkQPPQ4VQOpkdHaPBiOOzWFKsvHST2mlDVcltMRlbHjQ3/aH+ayEM8TbNg==',
    'yuidss': '7277640731678798175',
    'ymex': '1994158185.yrts.1678798185',
    'ys': 'svt.2#wprid.1678798460035042-5160156785138652246-vla1-3844-vla-l7-balancer-8080-BAL-3063#c_chck.2003355214',
    'yp': '1994158460.pcs.0#1679402865.mcv.0#1679402865.mcl.#1679402866.szm.1_25:1536x864:1495x723',
    '_ymab_param': 'uqo5chV1e74S26KwSMbgaPZhL0gN0ahoOj4Zky4tudUC2ddKx3Mp_JEn8M-lyvt7KcdKOLO9EP2WEUw5rYJVlUoZn9c',
    'device_id': 'b82ba91c6f3126d46082c7e136f057070c640ae5f',
    'active-browser-timestamp': '1678798684164',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'yabs-frequency=/5/0G00049ZfsC00000/; gdpr=0; _ym_uid=1671914309300264081; _ym_d=1671914314; yashr=1345913691675985995; is_gdpr=0; is_gdpr_b=CIG7UxDEqAEoAg==; _ym_isad=2; i=ff1yL/JpgXDnoTSyqGgM6ZjxPrAqw3j4SM3giCYvEvP3nmZ2k6bSFbAvgpTAu25EYufeo9rJ9iLRoUBAOp2yh11Ftwk=; yandexuid=7277640731678798175; _yasc=Lpj7B0xHIKUywkQPPQ4VQOpkdHaPBiOOzWFKsvHST2mlDVcltMRlbHjQ3/aH+ayEM8TbNg==; yuidss=7277640731678798175; ymex=1994158185.yrts.1678798185; ys=svt.2#wprid.1678798460035042-5160156785138652246-vla1-3844-vla-l7-balancer-8080-BAL-3063#c_chck.2003355214; yp=1994158460.pcs.0#1679402865.mcv.0#1679402865.mcl.#1679402866.szm.1_25:1536x864:1495x723; _ymab_param=uqo5chV1e74S26KwSMbgaPZhL0gN0ahoOj4Zky4tudUC2ddKx3Mp_JEn8M-lyvt7KcdKOLO9EP2WEUw5rYJVlUoZn9c; device_id=b82ba91c6f3126d46082c7e136f057070c640ae5f; active-browser-timestamp=1678798684164',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0 (Edition Yx GX)',
    'sec-ch-ua': '"Not=A?Brand";v="8", "Chromium";v="110", "Opera GX";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://music.yandex.ru/chart', cookies=cookies, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')