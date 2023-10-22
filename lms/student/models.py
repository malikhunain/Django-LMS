from django.db import models

# Create your models here.

#Student:
# name (CharField): The name of the student.
# student_id (CharField): A unique identifier for the student.
# email (EmailField): The student's email address.

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name