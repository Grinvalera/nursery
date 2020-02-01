from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Description, OurAnimal


def animals(request):
    all_our_animals = OurAnimal.objects.all()
    all_description = Description.objects.all()
    return render(request, 'animals/animals.html', locals())


def our_animals(request):
    return render(request, 'animals/1.html', locals())


# class DescriptionView(ListView):
  #  All_animals = Description.objects.all()
   # model = Description
    # template_name = 'animals/animals.html'
   # context_object_name = 'description'

# Create your views here.
