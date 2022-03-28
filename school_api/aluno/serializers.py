from rest_framework import serializers

from .models import Responsavel, Aluno, Nota


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = [
            'id',
            'nome',
            'cpf',
            'endereco',
            'telefone',
        ]
        read_only_fields = ['id']


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id',
            'nome',
            'ra',
            'data_nascimento',
            'turma',
            'endereco',
            'cpf',
            'telefone',
            'responsaveis',
            'notas',
        ]
        read_only_fields = ['id']


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = [
            'id',
            'aluno',
            'disciplina',
            'valor',
        ]
        read_only_fields = ['id']
