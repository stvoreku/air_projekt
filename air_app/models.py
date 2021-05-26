from django.db import models


# Create your models here.
class Place(models.Model):

    api = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    # TODO optimalization - consider long int vs float
    x = models.FloatField()
    y = models.FloatField()


class Queue(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.IntegerField()
    time = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    service_time = models.IntegerField()
    queue_length = models.IntegerField()
    current_queue_number = models.CharField(max_length=10)
