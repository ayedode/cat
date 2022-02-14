import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_image(url):

    response = urllib.request.urlopen(url)
    ParsedPage = BeautifulSoup(response,
                               'html.parser',
                               from_encoding=response.info().get_param('charset'))

    Image = ParsedPage.find("meta", property="og:image")["content"]
    return Image


def get_description(url):

    response = urllib.request.urlopen(url)
    ParsedPage = BeautifulSoup(response,
                               'html.parser',
                               from_encoding=response.info().get_param('charset'))
    Description = ParsedPage.find("meta", property="og:description")["content"]
    return Description

