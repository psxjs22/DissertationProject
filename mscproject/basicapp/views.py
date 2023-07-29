from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def consent(request):
    return render(request, 'consent.html')


def method(request):
    return render(request, 'method.html')