from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    #TODO optimalization - consider long int vs float
    x = models.FloatField()
    y = models.FloatField()

class Queue(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

