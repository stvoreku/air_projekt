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
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    service_time = models.IntegerField()  # TODO consider TimeFiled?
    queue_length = models.IntegerField()
    current_queue_number = models.CharField(max_length=10)
