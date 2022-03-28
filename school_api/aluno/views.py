from rest_framework import viewsets

from .filtersets import AlunoFilter, ResponsavelFilter
from .models import Responsavel, Aluno
from .serializers import (
    ResponsavelSerializer,
    AlunoSerializer,
)


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
    filterset_class = ResponsavelFilter


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filterset_class = AlunoFilter
