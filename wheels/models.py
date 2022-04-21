from django.db import models


# Create your models here.

class Rubber(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    season = models.CharField(max_length=20)
    width = models.IntegerField()
    profile = models.IntegerField()
    diametr = models.IntegerField()
    load_index = models.IntegerField()
    speed_index = models.CharField(max_length=1)
    # Speed index km/h:
    # L=120, M=130, N=140, P=150, Q=160, R=170, S=180, T=190, U=200, H=210, V=240, W=270, Y=300, Z=300+

    def __str__(self):
        return f"{self.brand} {self.model} - {self.width}/{self.profile}/{self.diametr} - {self.season}"


class Disc(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    color = models.CharField(max_length=50)
    width = models.FloatField(max_length=4)
    diametr = models.IntegerField()

    # load_index = models.PositiveIntegerField(max_length=3)
    # speed_index = models.CharField(max_length=1)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)

    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.diametr}"
