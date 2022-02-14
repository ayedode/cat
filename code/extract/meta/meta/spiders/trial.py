from meta_spider import MetaSpiderSpider
from loguru import logger
from scrapy.crawler import CrawlerProcess



obj=MetaSpiderSpider("https://www.google.com/")
logger.debug(obj.get_url())


process = CrawlerProcess(settings=None)
process.crawl(MetaSpiderSpider("https://www.google.com/"))
process.start()
