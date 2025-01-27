# Generated by Django 3.0.6 on 2020-06-04 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nationalites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_sexe', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_athlete', models.CharField(max_length=100)),
                ('prenom_athlete', models.CharField(max_length=42)),
                ('nationalite_athlete', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='nationalites.Nationalite')),
                ('sexe_athlete', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='athletes.Sexe')),
            ],
        ),
    ]
