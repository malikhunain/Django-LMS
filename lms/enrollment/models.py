from django.db import models
from student.models import Student
from course.models import Course

# Create your models here.
#Enrollment:
# student (ForeignKey to Student): Represent the student enrolling in a course.
# course (ForeignKey to Course): Represent the course in which a student is enrolled.
# enrollment_date (DateField): The date when the enrollment took place.

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.student) + ' ' + str(self.course)