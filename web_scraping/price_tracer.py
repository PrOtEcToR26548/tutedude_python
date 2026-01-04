import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
        self.response = requests.get(url= self.url, headers=self.user_agent)
        self.soup = BeautifulSoup(self.response.content, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found!"

    def product_price(self):
        price = self.soup.find("span", {'class': 'a-price-whole'})
        if price is not None:
            return price.text
        else:
            return "Tag not found!"
        
device = PriceTracer(url = "https://www.amazon.in/Samsung-Galaxy-Smartphone-Yellow-Storage/dp/B0CS5ZZMN8/ref=sr_1_1?dib=eyJ2IjoiMSJ9.O3xB_kiiFUsvf5zmsm5j4gUQpshlu6Jy9v44If1NOrPWPRcZk90rWHPJS-OEhuaA_Rr59oYy-NXxmoWDY7PufSTMVnhJ6qIII98fAMPvf-w0rJbcnLxpt2DL39EXaYR0VLDDBasEMu1PLjvgjcy25QrE60k9uPYSgqPKJEPnqUD6E5rNpTQkRiEFErwphvEIk8GzBGb2U--CoS4mBqCkez48kkwlow1RaMoycBAB77s.R3R-45B1LEHCtXewVdoeQTNbHjyNfMky1jKC1ayRKA4&dib_tag=se&keywords=s24&qid=1767537012&sr=8-1&th=1")

print(device.product_title())
print(device.product_price())