import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('table a::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, self.parse_pep)

    def parse_pep(self, response):
        number = response.url.split('/')[-2]
        name = response.css('h1.page-title::text')
        status = response.css('abbr::text').get()
        item = PepParseItem()
        item['number'] = (number[4:])
        item['name'] = name.get().split("–", 1)[-1].strip()
        item['status'] = status
        yield item
