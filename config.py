from fake_useragent import FakeUserAgent
from dotenv import load_dotenv
import os

load_dotenv() 

BOT_TOKEN = os.getenv("BOT_TOKEN")

CURRENCIES = [["TON", "тон"], 
              ["STARS", "старс"],
              ["USDT", "юсдт"]]

CURRENCY_ALIASES = {
    alias.lower(): group[0] 
    for group in CURRENCIES
    for alias in group
}

cookies = {
    'stel_ssid': 'f6d7b8029beb8d0e33_12568403534264444403',
    'stel_dt': '-180',
    'stel_ton_token': 'ucAvGdjj_SAUSk8agF6qVRr8zp7Pvy-4WbHdskmKpooXUFK_yEywnmoNkrgILa2J7kuA14qhVXBu0uR9_n7ZoJDsovhWlBR0Pg7xwAXE4ctLD_ReXr7xuLYH6i2t9MbWwmm-8hUdcg_8czgbtUNsJydUerD1RHSpdEX1ZhcLiC0gF0HKVYW0gtEqHdH93a8BJmnakXIQ',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://fragment.com',
    'priority': 'u=1, i',
    'referer': 'https://fragment.com/stars/buy?quantity=450',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': FakeUserAgent().random,
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'hash': '8f6d3729f36e300f7b',
}

data = {
    'stars': '0',
    'quantity': '100',
    'method': 'updateStarsPrices',
}
