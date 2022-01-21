import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_image(url):

    response = urllib.request.urlopen(url)
    ParsedPage = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'), headers={'User-Agent': 'Mozilla/5.0'})

    if ParsedPage.findAll("meta", property="og:image"):
        return ParsedPage.find("meta", property="og:image")["content"]
    else:
        return ("https://raw.githubusercontent.com/ayedode/cat/main/assests/no_image.png")


get_image("https://devops.com/2022-will-be-the-year-of-the-cyber-shift-show/")


