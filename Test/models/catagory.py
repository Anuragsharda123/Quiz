from django.db import models

class Catagory(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
