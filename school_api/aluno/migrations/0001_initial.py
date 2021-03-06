# Generated by Django 3.2.12 on 2022-03-27 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('ra', models.CharField(max_length=20, unique=True, verbose_name='Registro do Aluno (RA)')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=128, verbose_name='Endereço')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=128, verbose_name='Endereço')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Responsáveis',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='ResponsavelAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relacao', models.CharField(max_length=24, verbose_name='Relação')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.responsavel')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.PositiveSmallIntegerField(verbose_name='Valor')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.disciplina')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
                'ordering': ('aluno', 'disciplina', '-valor'),
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='notas',
            field=models.ManyToManyField(through='aluno.Nota', to='escola.Disciplina'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='responsaveis',
            field=models.ManyToManyField(through='aluno.ResponsavelAluno', to='aluno.Responsavel'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escola.turma'),
        ),
    ]
