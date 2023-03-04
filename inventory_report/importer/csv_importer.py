from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path) as csv:
            if path.split('.')[-1] == 'csv':
                return list(DictReader(csv))
            raise ValueError('Arquivo inválido')
