from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add helps to provide the current datetime

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# relation between student and course is M:M , so have created below separate or mapping table
# in class , we need to mention foreign key with class name
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateField(auto_now_add=True)


class TestTable(models.Model):
    name = models.CharField(max_length=100)

    class Meta: #Helps to do custom changes in our table
        db_table = 'test_table'
        ordering = ['-name']  # -name will be doing in desc order without - will be asc order





# CharField -> small sized text
# TextField -> large sized text
# IntegerField -> int values ...
# FloatField -> float values...
# BooleanField -> storing bool data
# DateTimeField -> for datetime format
# DateField -> for date format
# Foreign keys : used for 1 to many relationship