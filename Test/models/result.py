from django.db import models
from .test import Test
from .student import Student

class Result(models.Model):
    Test = models.ForeignKey(Test, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Rank = models.IntegerField(null=True)
    Total_Marks = models.IntegerField()
    Total_Attempted = models.IntegerField()
    Accuracy = models.IntegerField()