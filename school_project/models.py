from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=50)

    address = models.CharField(max_length=60)

    type = models.CharField(max_length=40)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)

    age = models.IntegerField()

    school = models.CharField(max_length=50)
              # ForeignKey(School, on_delete = models.CASCADE, related_name = 'students'))

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name