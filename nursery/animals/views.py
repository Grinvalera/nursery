from django.shortcuts import render, Http404, HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from .models import Description, OurAnimal


def our_animals(request, name):
    test = OurAnimal.objects.all()
    dog = get_object_or_404(OurAnimal, name=name)

    return render(request, 'animals/1.html', locals())


def animals(request):
    all_our_animals = OurAnimal.objects.all()
    all_description = Description.objects.all()
    return render(request, 'animals/animals.html', locals())


def test_def(request):
    return render(request, 'nursery/home.html', locals())


# class DescriptionView(ListView):
  #  All_animals = Description.objects.all()
   # model = Description
    # template_name = 'animals/animals.html'
   # context_object_name = 'description'

# Create your views here.
