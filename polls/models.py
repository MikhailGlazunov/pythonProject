from django.db import models
from django.urls import reverse


class Rating(models.IntegerChoices):
    VERYLOW = 1, '1'
    LOW = 2, '2'
    NORMAL = 3, '3'
    HIGH = 4, '4'
    VERYHIGH = 5, '5'


class Feedback(models.Model):
    author = models.CharField(max_length=20, verbose_name='Автор')
    text = models.CharField(max_length=120, verbose_name='Текст')
    rating = models.IntegerField(default=Rating.VERYLOW, choices=Rating.choices, verbose_name='Оценка')

    def get_absolute_url(self):
        return reverse('create')
