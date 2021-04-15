from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, null=True)
    points = models.PositiveIntegerField(default=0)
    isIn = models.BooleanField()

    def __str__(self):
        return self.name