# Generated by Django 4.1.3 on 2022-12-09 03:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
