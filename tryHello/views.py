import datetime

from django.http import HttpResponse
from django.shortcuts import render

from tryHello.models import Student


# Create your views here.

def hello_world(request,name):
    """ INSERT """
    #s1 = Student(name=name, age= 24, dob = datetime.date.today())
    #s1.save()  # save to db..

    """ SELECT """
    #all_students = Student.objects.all() # objects for all students Select * from table
    #print(all_students)


    student  = Student.objects.get(name=name) #  select * from table where name = name

    """ UPDATE """
    student.age = 10
    student.save()


    return HttpResponse('Hello Your age is ' + str(student.age) )
