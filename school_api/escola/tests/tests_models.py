from model_bakery import baker


def test_escola_str(db):
    escola = baker.make('escola.Escola')
    assert str(escola) == escola.nome
