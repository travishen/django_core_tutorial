from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import PostModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .forms import PostModelForm


@login_required()
def some_view(request):
    pass


def post_model_list_view(request):
    posts = PostModel.objects.all()
    # return HttpResponse(posts)
    template = 'blog/list-view.html'
    context = {
        "posts": posts
    }
    return render(request, template, context)


def post_model_detail_view(request, id=None):
    post = get_object_or_404(PostModel, id=id)

    template = 'blog/detail/detail.html'
    context = {
        'post': post
    }
    return render(request, template, context)


def post_model_create_view(request):
    form = PostModelForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        f = form.save(commit=False)
        # modify form.attributes here...
        f.save()
        messages.success(request, "Create a new post successfully!")
        # return HttpResponseRedirect('/blog/detail/{id}'.format(id=f.id))
        context = {
            'form': PostModelForm()
        }
    template = 'blog/create-view.html'

    return render(request, template, context)