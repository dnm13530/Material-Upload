# Generated by Django 5.0.1 on 2024-01-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0004_auto_20171022_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='feedback',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]