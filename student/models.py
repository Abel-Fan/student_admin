from django.db import models
from class_app.models import Class_app

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    sex = models.BooleanField(choices=(
        (1,'男'),
        (0,'女')
    ))
    class_id = models.ForeignKey(Class_app,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
