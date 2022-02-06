import scrapy
from loguru import logger

# import psycopg2
# from decouple import config




class MetaSpiderSpider(scrapy.Spider):
    name = 'meta_spider'
        

    start_urls = ['https://dzone.com/articles/site-reliability-engineer-sre-roles-and-responsibi']

    # print(start_urls)

    def parse(self, response):
        # print(response.css('title::text')[0].get())
        image_url = response.css(
            'meta[property="og:image"]::attr(content)')[0].get()
        description = response.css(
            'meta[property="og:description"]::attr(content)')[0].get()
        # title=response.css('meta[property="og:title"]::attr(content)')[0].get()
        # scrapy crawl meta_spider -o raw.json

        yield {
            'imageurl': image_url,
            'description': description
        }
        logger.debug(image_url)
        logger.debug(description)
        # return (image_url)
