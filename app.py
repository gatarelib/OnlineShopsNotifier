import requests
from bs4 import BeautifulSoup

request = requests.get("https://bit.ly/2E8LGBM")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"dir": "ltr", "data-price": "173999"})
print(element.text.strip())
# strip() method removes all trailing spaces
#<span dir="ltr" data-price="173999">173,999</span>
