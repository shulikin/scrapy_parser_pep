import datetime as dt
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
ENCODING = 'utf-8'
DATETIME = '%Y-%m-%d_%H-%M-%S'
DIR_SAVE = 'results'
STATUS = 'status'


class PepParsePipeline:

    statuses = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = self.statuses.get(item[STATUS], 0) + 1
        self.statuses[item[STATUS]] = status
        return item

    def close_spider(self, spider):

        res_dir = BASE_DIR / DIR_SAVE
        res_dir.mkdir(exist_ok=True)

        time = dt.datetime.now().strftime(DATETIME)
        filename = res_dir / f'status_summary_{time}.csv'
        with open(filename, mode='w', encoding=ENCODING, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('Статус', 'Количество'))
            for status, count in self.statuses.items():
                writer.writerow((status, count))
            writer.writerow(('Total', sum(self.statuses.values())))
