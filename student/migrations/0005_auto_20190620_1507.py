# Generated by Django 2.1.1 on 2019-06-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190620_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
    ]