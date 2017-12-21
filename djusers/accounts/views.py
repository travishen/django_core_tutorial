from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        pass
    return render(request, 'accounts/home.html', {})
