import requests
from bs4 import BeautifulSoup as bsoup
from pprint import pprint as pp

# doujin_code = input("Enter 6-digit code: ")
doujin_code = 390009
url = f"https://nhentai.net/g/{doujin_code}/"
r = requests.get(url)

soup = bsoup(r.text, features="html.parser")
title = soup.title.string.split("»")[0]

section = soup.find_all("section")
pp(section['id'])