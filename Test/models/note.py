from django.db import models

class Notes(models.Model):
    Title = models.CharField()
    document = models.FileField(upload_to='Assests/Notes/',)