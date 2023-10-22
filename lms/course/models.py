from django.db import models

# Create your models here.
# Course:
# title (CharField): The title of the course.
# description (TextField): A description of the course.
# instructor (CharField): The name of the course instructor.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.title