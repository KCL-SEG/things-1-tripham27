# Generated by Django 4.1.3 on 2022-12-09 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_thing_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
