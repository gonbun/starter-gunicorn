from django.shortcuts import render, redirect
from django.utils import timezone
# Create your views here.

def index(request):
    context = {'messages': "hello"}
    return render(request, 'calendar/index.html', context)