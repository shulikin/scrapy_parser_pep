from pathlib import Path

ALLOWED_DOMAIN = 'peps.python.org'
PROTOCOL = 'https://'
STATUS_SELECTOR = 'abbr::text'
TABLE_SELECTOR = 'table a::attr(href)'
TITLE_SELECTOR = 'h1.page-title::text'
BASE_DIR = Path(__file__).parent.parent
ENCODING = 'utf-8'
DATETIME = '%Y-%m-%d_%H-%M-%S'
DIR_SAVE = 'results'
STATUS = 'status'
SLASH = '/'

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = BOT_NAME + '.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
FEEDS = {
    DIR_SAVE + '/pep_%(time)s.csv': {
        'format': 'csv',
        'encoding': ENCODING,
        'store_empty': False,
        'fields': ['number', 'name', 'status'],
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
