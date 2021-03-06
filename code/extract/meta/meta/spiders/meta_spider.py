import scrapy
from loguru import logger
from scrapy.crawler import CrawlerProcess
import psycopg2
from decouple import config

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_HOST = config('DB_HOST')
DB_PASSWORD = config('DB_PASSWORD')

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
cur = conn.cursor()


def read_all():

    cur.execute("SELECT url FROM feed WHERE IMAGEURL IS NULL ;")
    rows = cur.fetchall()
    all_urls = []
    for row in rows:
        all_urls.append(str(row[0]))
    return(all_urls)


class MetaSpiderSpider(scrapy.Spider):
    name = 'meta_spider'

    start_urls = read_all()

    def parse(self, response):

        try:
            image_url = response.css(
                'meta[property="og:image"]::attr(content)')[0].get()
        except:
            logger.warning("NO IMAGE", response.url)
            image_url = "https://raw.githubusercontent.com/ayedode/cat/main/assests/no_image.png"

        try:
            description = response.css(
                'meta[property="og:description"]::attr(content)')[0].get()[:230]
        except:
            logger.warning("NO DESCRIPTION", response.url)
            description = "Not Available"

        title = response.css(
            'meta[property="og:title"]::attr(content)')[0].get()

        try:
            original_url = response.meta['redirect_urls'][0]
            logger.critical(original_url)
            # (parsed response) abcd.com/abcd -> cdn.abcd.com/abcd (database url)

        except:
            original_url = response.url
            logger.debug(original_url)
            # (parsed response) abcd.com/abcd -> abcd.com/abcd (no redirects)

        logger.info(response.url)
        logger.debug(original_url)
        logger.debug(image_url)
        logger.debug(description)

        cur.execute('UPDATE feed SET Description = %s, IMAGEURL = %s WHERE URL = %s;',
                    (description, image_url, original_url))

        logger.success("Updating  ", title)
        conn.commit()


process = CrawlerProcess(settings=None)
process.crawl(MetaSpiderSpider)
process.start()
