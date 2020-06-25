# Generated by Django 2.2.5 on 2020-05-21 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, unique=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDiagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(max_length=64)),
                ('id_num', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('genre', models.CharField(max_length=64)),
                ('occupation', models.CharField(max_length=64)),
                ('birthday', models.DateField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Entity')),
                ('list_diagnostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Diagnostic')),
            ],
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='type_diagnostic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.TypeDiagnostic'),
        ),
    ]