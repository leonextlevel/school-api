def test_responsavel_str(responsavel):
    assert str(responsavel) == responsavel.nome


def test_aluno_str(aluno):
    assert str(aluno) == aluno.nome


def test_nota_str(nota):
    assert str(nota) == f'{nota.valor} - {nota.aluno}'
