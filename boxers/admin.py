from django.contrib import admin
from .models import Genre, Boxer, Fights


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BoxerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'nick_name', 'genre')

class FightsAdmin(admin.ModelAdmin):
    list_display = ('red_boxer','blue_boxer','scheduled_rounds','result_round','fight_result','ight_winner')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Boxer, BoxerAdmin)
admin.site.register(Fights, FightsAdmin)
