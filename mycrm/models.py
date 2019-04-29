from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='课程')

    def __str__(self):
        return '%s:%s' % (self.name, self.course)


class Course(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='教师')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=64, verbose_name='名字')
    phone = models.IntegerField(verbose_name='电话')

    def __str__(self):
        return self.name
