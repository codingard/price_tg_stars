import requests
from bs4 import BeautifulSoup
from config import cookies, headers, params, data
class PriceStars:
    def __init__(self):
        self.stars_price_usdt = None
        self.stars_price_ton = None
        self._fetch_prices()

    def _fetch_prices(self):
        try:
            response = requests.post(
                'https://fragment.com/api',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data
            )
            response.raise_for_status()
            raw_data = response.json()
            cur_price_html = raw_data.get("cur_price", "")

            soup = BeautifulSoup(cur_price_html, 'html.parser')

            ton_div = soup.find("div", class_="tm-value")
            if ton_div:
                self.stars_price_ton = float(ton_div.get_text(strip=True)) / 100

            usdt_div = soup.find("div", class_="tm-radio-desc")
            if usdt_div:
                usdt_text = usdt_div.get_text(strip=True).replace("~", "").replace("\xa0", "").replace("$", "")
                self.stars_price_usdt = float(usdt_text) / 100

        except Exception as e:
            print(f"[ERROR] Не удалось получить цену STARS: {e}")
            self.stars_price_usdt = 0
            self.stars_price_ton = 0

    def ton_to_stars(self, ton: float) -> float:
        return ton / self.stars_price_ton if self.stars_price_ton else 0

    def usdt_to_stars(self, usdt: float) -> float:
        return usdt / self.stars_price_usdt if self.stars_price_usdt else 0

    def stars_to_ton(self, stars: float) -> float:
        return stars * self.stars_price_ton if self.stars_price_ton else 0

    def stars_to_usdt(self, stars: float) -> float:
        return stars * self.stars_price_usdt if self.stars_price_usdt else 0