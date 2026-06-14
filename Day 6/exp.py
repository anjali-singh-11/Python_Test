import requests
from bs4 import BeautifulSoup

url = "https://www.playstation.com/en-in/ps5/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text
print(f"Title: {title}")