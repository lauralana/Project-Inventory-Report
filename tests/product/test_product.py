from inventory_report.inventory.product import Product


def test_cria_produto():
    mock = Product(
        3,
        'NITROUS OXIDE',
        'Galena Biopharma',
        '2020-12-22',
        '2024-11-07',
        'CZ09 8588 0858 8435 9140 2695',
        'instrucao 3'
    )

    assert mock.id == 3
    assert mock.nome_do_produto == 'NITROUS OXIDE'
    assert mock.nome_da_empresa == 'Galena Biopharma'
    assert mock.data_de_fabricacao == '2020-12-22'
    assert mock.data_de_validade == '2024-11-07'
    assert mock.numero_de_serie == 'CZ09 8588 0858 8435 9140 2695'
    assert mock.instrucoes_de_armazenamento == 'instrucao 3'
