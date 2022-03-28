"""school_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from school_api.escola import views as views_escola
from school_api.aluno import views as views_aluno
from school_api.swagger import SwaggerView


router = routers.DefaultRouter()

# APP Aluno
router.register(r'aluno', views_aluno.AlunoViewSet)
router.register(r'responsavel', views_aluno.ResponsavelViewSet)

# APP Escola
router.register(r'escola', views_escola.EscolaViewSet)
router.register(r'turma', views_escola.TurmaViewSet)
router.register(r'professor', views_escola.ProfessorViewSet)
router.register(r'disciplina', views_escola.DisciplinaViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(title="Documentação - School API"), name="openapi-schema"),
    path('docs/', SwaggerView.as_view(), name='swagger-ui'),
]
