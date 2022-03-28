from school_api.aluno.serializers import AlunoSerializer


def test_aluno_serializer_representation_responsaveis(responsavel_aluno):
    serializer_data = AlunoSerializer(instance=responsavel_aluno.aluno).data
    assert serializer_data['responsaveis'] == [{
        'responsavel': responsavel_aluno.responsavel.id,
        'relacao': responsavel_aluno.relacao
    }]


def test_aluno_serializer_representation_notas(nota):
    serializer_data = AlunoSerializer(instance=nota.aluno).data
    assert serializer_data['notas'] == [{
        'disciplina': nota.disciplina.id,
        'valor': nota.valor
    }]
