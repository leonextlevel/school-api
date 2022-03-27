from django.contrib import admin

from .models import Escola, Professor, Disciplina, Turma, TurmaDisciplina

admin.site.register(Escola)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(TurmaDisciplina)
