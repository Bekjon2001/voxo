from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html', context={})

def products(request):
    return render(request, template_name='products.html', context={})