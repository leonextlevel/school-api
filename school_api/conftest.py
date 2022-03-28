import pytest

from model_bakery import baker


@pytest.fixture
def escola(db):
    return baker.make('escola.Escola')


@pytest.fixture
def turma(escola):
    return baker.make('escola.Turma', escola=escola)


@pytest.fixture
def professor(db):
    return baker.make('escola.Professor')


@pytest.fixture
def disciplina(professor):
    return baker.make('escola.Disciplina', professor=professor)


@pytest.fixture
def responsavel(db):
    return baker.make('aluno.Responsavel')


@pytest.fixture
def aluno(db):
    return baker.make('aluno.Aluno')


@pytest.fixture
def responsavel_aluno(responsavel, aluno):
    return baker.make('aluno.ResponsavelAluno', responsavel=responsavel, aluno=aluno)


@pytest.fixture
def nota(aluno, disciplina):
    return baker.make('aluno.Nota', aluno=aluno, disciplina=disciplina)
