# Generated by Django 2.1.1 on 2019-06-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.BooleanField(choices=[(1, '男'), (0, '女')]),
        ),
    ]
