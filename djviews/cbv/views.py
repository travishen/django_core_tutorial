from django.shortcuts import render


def home(request):
    return render(request, 'cbv/home.html', {})

