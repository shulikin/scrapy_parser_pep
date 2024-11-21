from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': ['number', 'name', 'status'],
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

ALLOWED_DOMAIN = 'peps.python.org'
START_URL = 'https://peps.python.org/'
STATUS_SELECTOR = 'abbr::text'
TABLE_SELECTOR = 'table a::attr(href)'
TITLE_SELECTOR = 'h1.page-title::text'
BASE_DIR = Path(__file__).parent.parent
ENCODING = 'utf-8'
DATETIME = '%Y-%m-%d_%H-%M-%S'
DIR_SAVE = 'results'
STATUS = 'status'
