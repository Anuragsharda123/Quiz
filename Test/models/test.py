from django.db import models

class Test(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Timing = models.PositiveIntegerField()
    num_Questions = models.PositiveIntegerField()
    Total_Marks = models.PositiveIntegerField()

    def __str__(self) :
        return self.Name