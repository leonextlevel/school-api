from django_filters import rest_framework as filters

from .models import Escola, Turma, Professor, Disciplina


class EscolaFilter(filters.FilterSet):

    class Meta:
        model = Escola
        fields = {
            'nome': ['icontains'],
            'endereco': ['icontains'],
        }


class TurmaFilter(filters.FilterSet):

    class Meta:
        model = Turma
        fields = {
            'ano': ['exact'],
            'periodo': ['exact'],
            'serie': ['exact'],
            'letra': ['exact'],
            'escola': ['exact'],
        }


class ProfessorFilter(filters.FilterSet):

    class Meta:
        model = Professor
        fields = {
            'nome': ['icontains'],
            'endereco': ['icontains'],
            'cpf': ['icontains'],
            'telefone': ['icontains'],
        }


class DisciplinaFilter(filters.FilterSet):

    class Meta:
        model = Disciplina
        fields = {
            'nome': ['icontains'],
            'professor': ['exact'],
        }
