from django.urls import path
from . import views

app_name = 'boxers'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:boxer_id>', views.detail, name='detail')
]
