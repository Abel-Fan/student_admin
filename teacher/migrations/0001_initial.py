# Generated by Django 2.1.1 on 2019-06-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_auto_20190620_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('project', models.CharField(max_length=20, verbose_name='课程')),
                ('student_id', models.ManyToManyField(to='student.Student')),
            ],
        ),
    ]
