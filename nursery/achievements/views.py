from django.shortcuts import render
from django.http import HttpResponse


def achievements(request):
    return render(request, 'achievements/achievements.html')
# Create your views here.
