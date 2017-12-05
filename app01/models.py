from django.db import models

# Create your models here.

class Userinfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)


class Lesson(models.Model):
    """
    班级表
    """
    title = models.CharField(max_length=16)#班级名称

class Student(models.Model):
    """
    学生表
    """
    name = models.CharField(max_length=16)#学生姓名

    student_lesson = models.ForeignKey(to=Lesson,related_name="student_lesson")#与班级为多对一的关系

class Questionnaire(models.Model):
    """
    问卷表
    """
    title = models.CharField(max_length=16)#问卷名
    questionnaire_lesson = models.ForeignKey(to=Lesson,related_name="questionnaire_lesson")#与班级的关系为多对一的关系

class Trouble(models.Model):
    """
    问题表
    """
    title=models.CharField(max_length=64)#问题名
    trouble_questionnaire=models.ForeignKey(to=Questionnaire,related_name="trouble_questionnaire")#与问卷表的关系为多对一的关系


class Genre(models.Model):
    """
    问题类型表
    """
    title=models.CharField(max_length=16)#类型名
    genre_trouble=models.ForeignKey(to=Trouble,related_name="genre_trouble")#与问题表为多对一的关系

class Option (models.Model):
    """
    选项表：关于问题的
    """
    title=models.CharField(max_length=64)#选项的内容
    option_trouble=models.ForeignKey(to=Trouble,related_name="option_trouble")


# ///////////以下是关于存数据的//////////
class Result(models.Model):
    """
    提交的结果表
    """
    content = models.CharField(max_length=32)#结果的值
    # result_option = models.ForeignKey(to=Option,related_name="result_option")#跟选项相关
    result_student=models.ManyToManyField(to=Student,related_name="result_student")#结果跟学生相关联
    result_trouble=models.ManyToManyField(to=Trouble,related_name="result_trouble")#跟问题向关联