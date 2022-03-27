# Generated by Django 3.2.12 on 2022-03-27 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=128, verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=128, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveSmallIntegerField(verbose_name='Ano')),
                ('periodo', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite'), ('integral', 'Integral')], max_length=8, verbose_name='Período')),
                ('serie', models.PositiveSmallIntegerField(choices=[(1, '1º ano - EF'), (2, '2º ano - EF'), (3, '3º ano - EF'), (4, '4º ano - EF'), (5, '5º ano - EF'), (6, '6º ano - EF'), (7, '7º ano - EF'), (8, '8º ano - EF'), (9, '9º ano - EF'), (10, '1º ano - EM'), (11, '2º ano - EM'), (12, '3º ano - EM')], verbose_name='Série')),
                ('letra', models.CharField(max_length=1, verbose_name='Letra')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ('escola', '-ano', 'serie', 'letra'),
            },
        ),
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.disciplina')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.turma')),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='disciplinas',
            field=models.ManyToManyField(through='escola.TurmaDisciplina', to='escola.Disciplina'),
        ),
        migrations.AddField(
            model_name='turma',
            name='escola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='escola.escola'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escola.professor'),
        ),
        migrations.AlterUniqueTogether(
            name='turma',
            unique_together={('ano', 'periodo', 'serie', 'letra', 'escola')},
        ),
    ]