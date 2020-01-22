from django.shortcuts import render
from django.http import HttpResponse

from .models import PictureCarousel, Title, LeftPictureSide, RightPictureSide


def home(request):
    left_side = LeftPictureSide.objects.all()
    right_side = RightPictureSide.objects.all
    nursery = Title.objects.all()
    carousel = PictureCarousel.objects.all()
    return render(request, 'nursery/home.html', locals())
# Create your views here.
