from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Product
from .models import user


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/detail.html", {"product": product})



RegisterForm = modelform_factory(user,exclude=[])

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "products/register.html", {"form" : form})
