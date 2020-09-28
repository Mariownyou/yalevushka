from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=200)
    is_visited = models.BooleanField()
    date = models.DateTimeField('date', auto_now_add=True)
    rare = models.IntegerField()
