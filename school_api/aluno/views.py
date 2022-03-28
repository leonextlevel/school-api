from rest_framework import viewsets

from .models import Responsavel, Aluno
from .serializers import (
    ResponsavelSerializer,
    AlunoSerializer,
)


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
