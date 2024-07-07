from django.db import models
from .test import Test

class Question(models.Model):
    Test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="test")
    Question = models.CharField(max_length=1000)
    Marks = models.IntegerField()

    def __str__(self) :
        return self.Question