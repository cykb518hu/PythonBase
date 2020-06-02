import requests
from bs4 import BeautifulSoup
response = requests.get("https://bbs.hupu.com/bxj")
soup = BeautifulSoup(response.text)
print(soup)
