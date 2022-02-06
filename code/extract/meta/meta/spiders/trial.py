from meta_spider import MetaSpiderSpider
import requests

# spider= MetaSpiderSpider()
# response= requests.get(spider.start_urls[0])

# print((spider.start_urls))
# spider.parse(response)


spider = MetaSpiderSpider("https://dzone.com/articles/site-reliability-engineer-sre-roles-and-responsibi")
print(spider.start_urls)