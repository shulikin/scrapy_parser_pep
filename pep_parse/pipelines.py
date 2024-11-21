import datetime as dt
import csv
from collections import defaultdict

from pep_parse.settings import (
    BASE_DIR,
    ENCODING,
    DATETIME,
    DIR_SAVE,
    STATUS,
)


class PepParsePipeline:
    def __init__(self):
        self.res_dir = BASE_DIR / DIR_SAVE
        self.res_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item[STATUS]] += 1
        return item

    def close_spider(self, spider):
        time = dt.datetime.now().strftime(DATETIME)
        filename = self.res_dir / f'status_summary_{time}.csv'
        with open(filename, mode='w', encoding=ENCODING, newline='') as f:
            writer = csv.writer(f)
            writer.writerows(
                (
                    ('Статус', 'Количество'),
                    *self.status_count.items(),
                    ('Всего', sum(self.status_count.values())),
                )
            )
