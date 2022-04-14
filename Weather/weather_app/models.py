from django.db import models

# Create your models here.
class CitySearch(models.Model):
    search = models.CharField(max_length=25)