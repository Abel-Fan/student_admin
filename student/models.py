from django.db import models
from class_app.models import Class_app
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator

from django.core.exceptions import ValidationError
# Create your models here.

def myValidate(value):
    if value!='abc':
        raise ValidationError("不是abc",params={'value':value})


class Student(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="姓名",
        null=False,blank=False,
        error_messages={
            'blank':'blank',
            'null':'null',
            'm1':'不好意思，不能小于10',
            'm2':"不能是除字母以外的数据"
        },
        help_text="请输入您姓名",
        validators=[
            MinLengthValidator(limit_value=2,message="不能小于十"),
            MaxLengthValidator(limit_value=10),
            # RegexValidator(regex="[a-z]+",message="只能是字母",code="m2"),
            # myValidate

        ])
    age = models.CharField(max_length=3)
    sex = models.BooleanField(choices=(
        (1,'男'),
        (0,'女')
    ))

    class_id = models.ForeignKey(Class_app,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
