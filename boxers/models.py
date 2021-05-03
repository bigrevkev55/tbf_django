from django.db import models
from django.db.models.deletion import CASCADE
#from django.utils import timezone

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


class Fights(models.Model):
    fight_date = models.DateField()
    red_boxer = models.ManyToManyField(
        Boxer, through='Boxer_fights')
    blue_boxer = models.ManyToManyField(
        Boxer, through='Boxer_fights')
    scheduled_rounds = models.CharField
    result_round = models.IntegerField()
    fight_result = models.CharField()
    fight_winner = models.ManyToManyField(
        Boxer, through='Boxer_fights')

    def __str__(self):
        return self.fight_id


class Boxer_fights(models.Model):
    boxer = models.ForeignKey(Boxer, on_delete=models.CASCADE)
    fight = models.ForeignKey(Fights, on_delete=models.CASCADE)
