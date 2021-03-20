import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# command to run: scrapy runspider emily/spiders/emily-spider.py -o emily.json


class PoemItem(scrapy.Item):
    poem_title = scrapy.Field()
    poem_text = scrapy.Field()


class PoemSpider(CrawlSpider):
    name = "poems"
    allowed_domains = ["www.bartleby.com"]
    start_urls = ["https://www.bartleby.com/113/indexlines.html"]

    rules = (Rule(LinkExtractor(allow=("113")), callback="parse_item"),)

    def parse_item(self, response):
        item = PoemItem()
        item["poem_title"] = response.xpath("//title/text()").get()
        item["poem_text"] = response.xpath(
            "//table/tbody/tr/td/table/tbody/tr/td/text()"
        ).getall()

        return item
