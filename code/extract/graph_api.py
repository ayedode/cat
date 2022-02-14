import json
import requests
from decouple import config


access_token = config('GRAPH_API_TOKEN')
api_endpoint = config('GRAPH_API_ENDPOINT')


# r = requests.post(request)
# call = r.content
# json_data = json.loads(call)
# url = json_data['url']
# title = json_data['title']
# description = json_data['description']


def get_image_from_graph(url):

    request = api_endpoint+url+"?access_token="+access_token
    r = requests.post(request)
    call = r.content
    json_data = json.loads(call)
    Image = json_data['image'][0]['url']
    return Image


def get_description_from_graph(url):

    request = api_endpoint+url+"?access_token="+access_token
    r = requests.post(request)
    call = r.content
    json_data = json.loads(call)
    Description = json_data['description']
    return Description
