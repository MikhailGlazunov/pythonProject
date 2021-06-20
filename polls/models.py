from django.db import models


class Rating(models.IntegerChoices):
    LOW = 1, '1'
    NORMAL = 2, '2'
    HIGH = 3, '3'
    VHIGH = 4, '4'
    VVHIGH = 5, '5'


class Feedback(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=120)
    rating = models.IntegerField(default=Rating.LOW, choices=Rating.choices)
