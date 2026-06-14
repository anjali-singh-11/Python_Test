import requests
from bs4 import BeautifulSoup

url = "https://www.playstation.com/en-in/ps5/"
response = requests.get(url)

# HTML ko parse kro
soup = BeautifulSoup(response.text, "html.parser")

# Title nikalo
title = soup.title.text
print(f"Title: {title}")

h1 = soup.find("h1")
print(f"H1: {h1.text}")

p = soup.find("p")
print(f"Paragraph: {p.text}")

links = soup.findAll("a")

for link in links:
    print(link.text)
    print(link.get)("href")