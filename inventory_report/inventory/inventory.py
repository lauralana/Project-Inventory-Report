import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def get_files(self, path):
        with open(path) as file:
            report = []
            if path.split('.')[-1] == 'json':
                report = json.load(file)
            elif path.split('.')[-1] == 'csv':
                report = list(csv.DictReader(file))
            elif path.split('.')[-1] == 'xml':
                xml = ET.parse(file).getroot()
                for i in xml:
                    report.append({
                        "id": i.find("id").text,
                        "nome_do_produto": i.find("nome_do_produto").text,
                        "nome_da_empresa": i.find("nome_da_empresa").text,
                        "data_de_fabricacao": i.find(
                            "data_de_fabricacao").text,
                        "data_de_validade": i.find("data_de_validade").text,
                        "numero_de_serie": i.find("numero_de_serie").text,
                        "instrucoes_de_armazenamento": i.find(
                            "instrucoes_de_armazenamento").text
                    })
            return report

    @classmethod
    def import_data(self, path: str, type: str) -> str:
        report = ''
        files = self.get_files(self, path)
        report = SimpleReport if type == 'simples' else CompleteReport
        return report.generate(files)
