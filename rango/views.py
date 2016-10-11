from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': categories}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html', {"my_name": "Heriyanto"})