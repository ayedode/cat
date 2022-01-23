import json
import requests
from decouple import config


access_token = config('GRAPH_API_TOKEN')
api_endpoint = config('GRAPH_API_ENDPOINT')

url = "https://devops.com/2022-will-be-the-year-of-the-cyber-shift-show/"


request = api_endpoint+url+"?access_token="+access_token


# r = requests.post(request)
# call = r.content
# json_data = json.loads(call)
# url = json_data['url']
# title = json_data['title']
# description = json_data['description']


def get_image(url):

    request = api_endpoint+url+"?access_token="+access_token
    r = requests.post(request)
    call = r.content
    json_data = json.loads(call)
    image = json_data['image'][0]['url']
    return image



def get_description(url):

    request = api_endpoint+url+"?access_token="+access_token
    r = requests.post(request)
    call = r.content
    json_data = json.loads(call)
    description = json_data['description']
    return description


print(get_description(url))
