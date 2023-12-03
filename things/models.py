from django.db import models

# Create your models here.
class Things(models.Model):
    name = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    description = models.CharField(max_length = 500)
    