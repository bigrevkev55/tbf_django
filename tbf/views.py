from django.shortcuts import render
from crudbuilder import views

def home(request):
    return render(request, 'home.html')



views.ViewBuilder()