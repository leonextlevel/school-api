from rest_framework import viewsets

from .filtersets import (
    EscolaFilter,
    TurmaFilter,
    ProfessorFilter,
    DisciplinaFilter,
)
from .models import Escola, Turma, Professor, Disciplina
from .serializers import (
    EscolaSerializer,
    TurmaSerializer,
    ProfessorSerializer,
    DisciplinaSerializer,
)


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    filterset_class = EscolaFilter


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    filterset_class = TurmaFilter


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filterset_class = ProfessorFilter


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    filterset_class = DisciplinaFilter
