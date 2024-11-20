import csv
import datetime as dt

from pep_parse.constants import ARG


class PepParsePipeline:

    statuses = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = self.statuses.get(item[ARG.STATUS], 0) + 1
        self.statuses[item[ARG.STATUS]] = status
        return item

    def close_spider(self, spider):

        res_dir = ARG.DIR_SAVE
        res_dir.mkdir(exist_ok=True)

        time = dt.datetime.now().strftime(ARG.DATETIME)
        filename = res_dir / f'status_summary_{time}.csv'
        with open(filename, mode='w', encoding=ARG.ENCODING, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('Статус', 'Количество'))
            for status, count in self.statuses.items():
                writer.writerow((status, count))
            writer.writerow(('Total', sum(self.statuses.values())))
