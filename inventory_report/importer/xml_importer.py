from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path) as xml:
            if path.split('.')[-1] == 'xml':
                root = ET.parse(xml).getroot()
                report = []
                for i in root:
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
            raise ValueError('Arquivo inválido')
