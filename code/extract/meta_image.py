import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_image(url):

    response = urllib.request.urlopen(url)
    ParsedPage = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'))

    if ParsedPage.findAll("meta", property="og:image"):
        return ParsedPage.find("meta", property="og:image")["content"]
    else:
        return ("https://raw.githubusercontent.com/ayedode/cat/main/assests/no_image.png")

