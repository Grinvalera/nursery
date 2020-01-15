from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Description


def animals(request):
    all = Description.objects.all()
    return render(request, 'animals/animals.html', locals())



# class DescriptionView(ListView):
  #  All_animals = Description.objects.all()
   # model = Description
    # template_name = 'animals/animals.html'
   # context_object_name = 'description'

# Create your views here.
