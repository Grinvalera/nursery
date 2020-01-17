from django.shortcuts import render
from django.http import HttpResponse

from .models import PictureCarousel


def home(request):
    all = PictureCarousel.objects.all()
    return render(request, 'news/news.html', locals())
# Create your views here.
