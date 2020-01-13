from django.shortcuts import render
from .forms import SubscriberForm
from products import models


def landing(request):
    name = "Pavel"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = models.ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, 'landing/home.html', locals())
