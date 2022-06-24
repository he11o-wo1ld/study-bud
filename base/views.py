from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Lets learn python'},
    {'id': 3, 'name': 'Lets learn python'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)
