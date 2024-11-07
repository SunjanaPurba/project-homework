from django.db import models

class Student(models.Model):
    university_name = models.CharField(max_length=200)
    name = models.CharField(max_length=170)
    student_id = models.IntegerField()
    department = models.CharField(max_length=150)

    def __str__(self):
        return self.name

