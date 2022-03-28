def test_escola_str(escola):
    assert str(escola) == escola.nome


def test_turma_str(turma):
    assert str(turma) == f'{turma.get_serie_display()} - {turma.letra} ({turma.ano})'


def test_professor_str(professor):
    assert str(professor) == professor.nome


def test_disciplina_str(disciplina):
    assert str(disciplina) == disciplina.nome
