from django.shortcuts import render

from .forms import SearchForm, TestForm, PostModelForm

from .models import PostModel

from django.http import HttpResponseRedirect

from django.forms import formset_factory, modelformset_factory


def search(request):
    form = SearchForm()
    return render(request, 'blog/search.html', {'form': form})


def test(request):

    # get data via html form

    # form = TestForm()
    # if request.method == 'POST':
    #     user_name = request.POST.get('user_name')

    # get data via django form

    data = request.POST or None
    user = request.user
    initial = {
        'user_name': user.username,
        'is_root': True
    }

    form = TestForm(data=data, user=user, initial=initial)

    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')

    return render(request, 'blog/test.html', {'form': form})


def post(request):

    data = request.POST or None

    form = PostModelForm(data=data)

    if form.is_valid():
        if form.cleaned_data:
            form.save()

    return render(request, 'blog/test.html', {'form': form})


def formset(request):

    test_formset = modelformset_factory(PostModel, fields=['title', 'active'])

    data = request.POST or None

    if request.user.is_authenticated():
        queryset = PostModel.objects.filter(author_email__icontains=request.user)
    else:
        queryset = None

    forms = test_formset(data=data, queryset=None)

    if forms.is_valid():
        for form in forms:
            form.save()

    context = {
        'forms': forms
    }
    return render(request, 'blog/formset.html', context)



