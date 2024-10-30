import datetime

from database_test.models import Student
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def db_commands(request,name):
    """ INSERT """
    #s1 = Student(name=name, age= 24, dob = datetime.date.today())
    #s1.save()  # save to db..
    #print(s1.age)
    """ SELECT """
    # all_students = Student.objects.all() # objects for all students Select * from table
    # print(all_students)

    student = Student.objects.get(name=name)  # select * from table where name = name

    """ UPDATE """
    student.age = 20
    student.save()

    return HttpResponse('Hello Your age is ' + str(student.age))
