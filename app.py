__author__='libere'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://bit.ly/2E8LGBM")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"dir": "ltr", "data-price": "173999"})
string_price = element.text.strip() 
#"Price"


# strip() method removes all trailing spaces around the element.text
# tag required <span dir="ltr" data-price="173999">173,999</span>
