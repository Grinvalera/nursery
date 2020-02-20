"""nursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, pa'th
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from .views import animals, our_animals
from django.views.generic import DetailView
from .models import OurAnimal


urlpatterns = [
    path(r'', animals, name='animals'),
    url(r'^(?P<pk>\w+)/$', DetailView.as_view(model=OurAnimal, template_name='animals/2.html'), name='our_animal')
    # url(r'^baron', views.test_def, name='test_def'),

]
