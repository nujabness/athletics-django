# Generated by Django 3.0.6 on 2020-06-04 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_phase', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_type', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_epreuve', models.CharField(max_length=42)),
                ('phase_epreuve', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='epreuves.Phase')),
                ('type_epreuve', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='epreuves.Type')),
            ],
        ),
    ]
