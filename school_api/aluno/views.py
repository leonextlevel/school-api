from rest_framework import generics
from rest_framework import viewsets

from .filtersets import AlunoFilter, ResponsavelFilter
from .models import Responsavel, Aluno
from .serializers import (
    ResponsavelSerializer,
    AlunoSerializer,
    NotaSerializer,
)


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    filterset_class = ResponsavelFilter


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filterset_class = AlunoFilter


class NotaCreateView(generics.CreateAPIView):
    '''
    Endpoint para inserir um nota para um aluno em uma disciplina.
    '''
    serializer_class = NotaSerializer
