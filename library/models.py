from django.db import models
from django.utils import timezone


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=23)
    address = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(default=timezone.now)
    edition = models.CharField(max_length=100)

