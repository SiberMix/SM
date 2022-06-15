
from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=35)

    def __str__(self):
        return self.position
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
class City(models.Model):
    city = models.CharField(max_length=35)

    def __str__(self):
        return self.city
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

