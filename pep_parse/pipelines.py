import datetime as dt
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    statuses = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = self.statuses.get(item['status'], 0) + 1
        self.statuses[item['status']] = status
        return item

    def close_spider(self, spider):

        res_dir = BASE_DIR / 'results'
        res_dir.mkdir(exist_ok=True)

        time = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = res_dir / f'status_summary_{time}.csv'
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('Статус', 'Количество'))
            for status, count in self.statuses.items():
                writer.writerow((status, count))
            writer.writerow(('Total', sum(self.statuses.values())))
