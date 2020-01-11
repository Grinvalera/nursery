from django.shortcuts import render


def back(request):
    return render(request, 'animals/animals.html')
# Create your views here.
