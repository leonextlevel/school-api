from django.db import models


class Responsavel(models.Model):
    nome = models.CharField('Nome', max_length=64)
    endereco = models.CharField('Endereço', max_length=128)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    telefone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'
        ordering = ('nome',)

    def __str__(self) -> str:
        return self.nome


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=64)
    ra = models.CharField('Registro do Aluno (RA)', max_length=20, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    turma = models.ForeignKey('escola.Turma', on_delete=models.PROTECT, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=128)
    cpf = models.CharField('CPF', max_length=14, unique=True, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=15, null=True, blank=True)

    responsaveis = models.ManyToManyField(
        Responsavel,
        through='ResponsavelAluno',
        through_fields=('aluno', 'responsavel')
    )

    notas = models.ManyToManyField(
        'escola.Disciplina',
        through='Nota',
        through_fields=('aluno', 'disciplina')
    )

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ('nome',)

    def __str__(self) -> str:
        return self.nome


class ResponsavelAluno(models.Model):
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    relacao = models.CharField('Relação', max_length=24)


class Nota(models.Model):
    disciplina = models.ForeignKey('escola.Disciplina', on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.PositiveSmallIntegerField('Valor')

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ('aluno', 'disciplina', '-valor')

    def __str__(self) -> str:
        return f'{self.valor} - {self.aluno}'
