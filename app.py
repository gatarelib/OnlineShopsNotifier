__author__='libere'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://bit.ly/2E8LGBM")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"dir": "ltr", "data-price": "173999"})
string_price = element.text.strip()  #"Price"

price_without_symbol = string_price[1:] # copies everything from start of tring_price to string price_without_symbol except the first item
# The above method optimizes memory

print(float(price_without_symbol) < 16000)

price = float(price_without_symbol)

if price < 16000:
  print("Buy the phone")
  print("The current price is {}".format(string_price))
 else:
  print("Do not buy its too expensive")

# strip() method removes all trailing spaces around the element.text
# tag required <span dir="ltr" data-price="173999">173,999</span>
