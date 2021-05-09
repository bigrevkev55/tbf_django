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


class Fight(models.Model):
    fight_date = models.DateField()
    red_boxer = models.ManyToManyField(
        through='.Boxer_fights',
        through_fields=('red_boxer', 'fight'))
    blue_boxer = models.ManyToManyField(
        through='.Boxer_fights',
        through_fields=('blue_boxer', 'fight'))
    scheduled_rounds = models.CharField
    result_round = models.IntegerField()
    fight_result = models.CharField(max_length=255)
    fight_winner = models.ManyToManyField(
        through='.Boxer_fights',
        through_fields=('boxer', 'fight'))

    def __str__(self):
        return str(self.fight_id)


class Boxer_fights(models.Model):
    red_boxer = models.ForeignKey(Boxer, on_delete=models.CASCADE)
    blue_boxer = models.ForeignKey(Boxer, on_delete=models.CASCADE)
    fight = models.ForeignKey(Fights, on_delete=models.CASCADE)

    def __str__(self):
        return str(Boxer_fights.id)
