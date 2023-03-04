from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock = Product(
        '3',
        'NITROUS OXIDE',
        'Galena Biopharma',
        '2020-12-22',
        '2024-11-07',
        'CZ09 8588 0858 8435 9140 2695',
        'instrucao 3'
    )

    assert str(mock) == (
        'O produto NITROUS OXIDE fabricado em 2020-12-22 '
        'por Galena Biopharma com validade até 2024-11-07 precisa '
        'ser armazenado instrucao 3.'
        )
