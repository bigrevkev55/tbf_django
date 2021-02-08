from django.contrib import admin
from .models import Genre, Boxer


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BoxerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'nick_name', 'genre')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Boxer, BoxerAdmin)
