from rest_framework import serializers

from .models import Escola, Turma, Professor, Disciplina


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = [
            'id',
            'nome',
            'endereco'
        ]
        read_only_fields = ['id']


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
            'id',
            'ano',
            'periodo',
            'serie',
            'letra',
            'escola',
            'disciplinas',
        ]
        read_only_fields = ['id']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = [
            'id',
            'nome',
            'cpf',
            'endereco',
            'telefone',
        ]
        read_only_fields = ['id']


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = [
            'id',
            'nome',
            'professor',
        ]
        read_only_fields = ['id']
