from inventory_report.importer.importer import Importer
from json import load


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path) as json:
            if path.split('.')[-1] == 'json':
                return load(json)
            raise ValueError('Arquivo inválido')
