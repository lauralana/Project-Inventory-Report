from datetime import datetime
from collections import Counter
from typing import List


class SimpleReport:
    @staticmethod
    def generate(inventory: List[dict]) -> str:
        oldest_date = min([row['data_de_fabricacao'] for row in inventory])
        company = Counter([row['nome_da_empresa'] for row in inventory])
        expiration_date = min([row['data_de_validade'] for row in inventory
                              if (row['data_de_validade'] > datetime.now()
                               .strftime('%Y-%m-%d'))])

        return(
            'Data de fabricação mais antiga: {}\n'
            'Data de validade mais próxima: {}\n'
            'Empresa com mais produtos: {}'
        ).format(oldest_date, expiration_date, company.most_common()[0][0])
