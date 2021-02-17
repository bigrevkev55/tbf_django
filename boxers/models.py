from django.db import models
from django.utils import timezone
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Boxer(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)
    #date_of_birth = models.DateField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.last_name
