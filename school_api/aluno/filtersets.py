from django_filters import rest_framework as filters

from .models import Aluno, Responsavel


class AlunoFilter(filters.FilterSet):

    data_nascimento_gte = filters.DateFilter(field_name='data_nascimento', lookup_expr=('gte'))
    data_nascimento_lte = filters.DateFilter(field_name='data_nascimento', lookup_expr=('lte'))

    class Meta:
        model = Aluno
        fields = {
            'nome': ['icontains'],
            'ra': ['icontains'],
            'turma': ['exact'],
            'endereco': ['icontains'],
            'cpf': ['icontains'],
            'telefone': ['icontains'],
        }


class ResponsavelFilter(filters.FilterSet):

    class Meta:
        model = Responsavel
        fields = {
            'nome': ['icontains'],
            'endereco': ['icontains'],
            'cpf': ['icontains'],
            'telefone': ['icontains'],
        }
