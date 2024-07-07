from django.db import models

class Test(models.Model):
    Name = models.CharField(max_length=30, unique=True)

    def __str__(self) :
        return self.Name