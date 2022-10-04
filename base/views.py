from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, 'base/home.html')


def forms(request):
    pass
