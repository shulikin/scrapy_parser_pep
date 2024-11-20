from pathlib import Path


class ARG:

    ALLOWED_DOMAIN = 'peps.python.org'
    START_URL = 'https://peps.python.org/'
    NAME_SPIDER = 'pep'

    ENCODING = 'utf-8'
    DATETIME = '%Y-%m-%d_%H-%M-%S'
    DIR_SAVE = Path(__file__).parent.parent / 'results'
    STATUS = 'status'

    STATUS_SELECTOR = 'abbr::text'
    TABLE_SELECTOR = 'table a::attr(href)'
    TITLE_SELECTOR = 'h1.page-title::text'
