import requests
from bs4 import BeautifulSoup


url = "https://www.p3r.one/gpt-j/"
r = requests.get(url=url)
# Create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.find("meta"))
