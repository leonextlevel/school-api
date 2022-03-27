from django.contrib import admin

from .models import Responsavel, Aluno, ResponsavelAluno, Nota

admin.site.register(Responsavel)
admin.site.register(Aluno)
admin.site.register(ResponsavelAluno)
admin.site.register(Nota)
