from django.db import models


class Escola(models.Model):
    nome = models.CharField('Nome', max_length=64)
    endereco = models.CharField('Endereço', max_length=128)

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
        ordering = ('nome',)
    
    def __str__(self) -> str:
        return self.nome


class Professor(models.Model):
    nome = models.CharField('Nome', max_length=64)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    endereco = models.CharField('Endereço', max_length=128)
    telefone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ('nome',)

    def __str__(self) -> str:
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=64)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ('nome',)

    def __str__(self) -> str:
        return self.nome


class Turma(models.Model):

    class PeriodoChoices(models.TextChoices):
        MANHA = 'manha', 'Manhã'
        TARDE = 'tarde', 'Tarde'
        NOITE = 'noite', 'Noite'
        INTEGRAL = 'integral', 'Integral'

    class SerieChoices(models.IntegerChoices):
        ANO_1 = 1, '1º ano - EF'
        ANO_2 = 2, '2º ano - EF'
        ANO_3 = 3, '3º ano - EF'
        ANO_4 = 4, '4º ano - EF'
        ANO_5 = 5, '5º ano - EF'
        ANO_6 = 6, '6º ano - EF'
        ANO_7 = 7, '7º ano - EF'
        ANO_8 = 8, '8º ano - EF'
        ANO_9 = 9, '9º ano - EF'
        ANO_1_MEDIO = 10, '1º ano - EM'
        ANO_2_MEDIO = 11, '2º ano - EM'
        ANO_3_MEDIO = 12, '3º ano - EM'

    ano = models.PositiveSmallIntegerField('Ano')
    periodo = models.CharField('Período', max_length=8, choices=PeriodoChoices.choices)
    serie = models.PositiveSmallIntegerField('Série', choices=SerieChoices.choices)
    letra = models.CharField('Letra', max_length=1, )
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT)

    disciplinas = models.ManyToManyField(Disciplina, through='TurmaDisciplina')

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ('escola', '-ano', 'serie', 'letra')
        unique_together = (
            'ano',
            'periodo',
            'serie',
            'letra',
            'escola',
        )

    def __str__(self) -> str:
        return f'{self.get_serie_display()} - {self.letra} ({self.ano})'


class TurmaDisciplina(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
