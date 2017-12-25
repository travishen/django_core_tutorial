from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404

from .forms import UserCreationForm, UserLoginForm

from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required

from .models import ActivationProfile
# Create your views here.


@login_required
def home(request):
    template = 'accounts/home.html'
    return render(request, template, {})


def user_login(request, *args, **kwargs):
    template = 'accounts/login.html'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect('/')
    context = {
        'form': form
    }

    return render(request, template, context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')


def register(request, *args, **kwargs):
    template = 'accounts/register.html'
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, template, context)


def user_activate(request, code=None, *args, **kwargs):

    q = ActivationProfile.objects.filter(key=code)

    if q.exists() and q.count() == 1:
        act_obj = q.first()
        if not act_obj.expired:
            user_obj = act_obj.user
            user_obj.is_active = True
            user_obj.save()
            act_obj.expired = True
            act_obj.save()
        return HttpResponseRedirect('/accounts/login')
    else:
        raise Http404
