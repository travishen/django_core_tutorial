from django.shortcuts import render

from .forms import SearchForm, TestForm, PostModelForm


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
        form.save()

    return render(request, 'blog/test.html', {'form': form})
