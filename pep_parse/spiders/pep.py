import scrapy

from pep_parse.items import PepParseItem

from pep_parse.settings import (
    ALLOWED_DOMAIN,
    START_URL,
    STATUS_SELECTOR,
    TABLE_SELECTOR,
    TITLE_SELECTOR,
)


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAIN]
    start_urls = [START_URL]

    def parse(self, response):
        pep_links = response.css(TABLE_SELECTOR).getall()
        for link in pep_links:
            yield response.follow(link, self.parse_pep)

    def parse_pep(self, response):
        number = response.url.split('/')[-2]
        name = response.css(TITLE_SELECTOR)
        status = response.css(STATUS_SELECTOR).get()
        item = PepParseItem()
        item['number'] = (number[4:])
        item['name'] = name.get().split("–", 1)[-1].strip()
        item['status'] = status
        yield item
