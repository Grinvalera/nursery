from django.shortcuts import render


def animals(request):
    return render(request, 'animals/animals.html')
# Create your views here.
