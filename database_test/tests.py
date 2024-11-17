from django.test import TestCase

# Create your tests here.


from database_test.models import Enrollment
from django.db import connection

enrolls = Enrollment.objects.all()

for enroll in enrolls:
    print(enroll.course.name)
    print(enroll.student.name)

print(len(connection.queries))

print(connection.queries)


enrolls = Enrollment.objects.prefetch_related('course', 'student')

for enroll in enrolls:
    print(enroll.course.name)
    print(enroll.student.name)
