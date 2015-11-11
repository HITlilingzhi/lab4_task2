from django.db import models

# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=30)
    AuthorID = models.CharField(max_length=30)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.CharField(max_length=20)
    Price = models.CharField(max_length=10)

class Author(models.Model):
    AuthorID = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=3)
    Country = models.CharField(max_length=20)