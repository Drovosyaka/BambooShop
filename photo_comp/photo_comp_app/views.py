import requests
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from .models import *
from django.views.generic import CreateView

from photo_comp_main.models import *


def vape_juice(request):
    object_models = Products.objects.filter(category=4)
    return render(request, 'vape_juice.html', {'object_models': object_models})


def disposable(request):
    object_models = Products.objects.filter(category=1)
    return render(request, 'disposable.html', {'object_models': object_models})


def pod(request):
    object_models = Products.objects.filter(category=2)
    return render(request, 'pod.html', {'object_models': object_models})


def consumables(request):
    object_models = Products.objects.filter(category=3)
    return render(request, 'consumables.html', {'object_models': object_models})


def hookah(request):
    object_models = Products.objects.filter(category=5)
    return render(request, 'hookah.html', {'object_models': object_models})


def tobacco_free_mixtures(request):
    object_models = Products.objects.filter(category=6)
    return render(request, 'tobacco_free_mixtures.html', {'object_models': object_models})


def tobacco(request):
    object_models = Products.objects.filter(category=7)
    return render(request, 'tobacco.html', {'object_models': object_models})


def goal(request):
    object_models = Products.objects.filter(category=8)
    return render(request, 'goal.html', {'object_models': object_models})


def accessory(request):
    object_models = Products.objects.filter(category=9)
    return render(request, 'accessory.html', {'object_models': object_models})


def test(request):
    return render(request, 'test.html')


def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user_name=Basket.user_name, id=product_id)

    if not baskets.exists():
        Basket.objects.create(user_name='Maksimka', product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def home(request):
    api_url = 'http://127.0.0.1:8000/api/v1/photocomp/'
    response = requests.get(api_url)
    data = response.json()

    return render(request, 'main.html', {'data': data})


def profile(request):
    user = request.user
    photos = Categories.objects.filter(user=user)
    return render(request, 'profile.html', {'photos': photos})
