# Generated by Django 3.0.6 on 2020-06-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nationalite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_nationalite', models.CharField(max_length=100)),
                ('link_nationalite', models.CharField(max_length=100)),
            ],
        ),
    ]
