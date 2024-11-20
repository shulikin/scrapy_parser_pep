import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import ARG


class PepSpider(scrapy.Spider):

    name = ARG.SNAME_SPIDER
    allowed_domains = [ARG.ALLOWED_DOMAIN]
    start_urls = [ARG.START_URL]

    def parse(self, response):
        pep_links = response.css(ARG.TABLE_SELECTOR).getall()
        for link in pep_links:
            yield response.follow(link, self.parse_pep)

    def parse_pep(self, response):
        number = response.url.split('/')[-2]
        name = response.css(ARG.TITLE_SELECTOR)
        status = response.css(ARG.STATUS_SELECTOR).get()
        item = PepParseItem()
        item['number'] = (number[4:])
        item['name'] = name.get().split("–", 1)[-1].strip()
        item['status'] = status
        yield item
