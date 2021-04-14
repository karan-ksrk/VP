from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, null=True)
    points = models.IntegerField(null=True, default=0)
    isIn = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name