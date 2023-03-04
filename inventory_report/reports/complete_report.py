from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        response = super().generate(inventory)
        company = Counter(row['nome_da_empresa'] for row in inventory)
        in_stock = ''
        for key, value in company.items():
            in_stock += f'- {key}: {value}\n'
        return (response + '\n' + 'Produtos estocados por empresa:\n{}'
                ).format(in_stock)
