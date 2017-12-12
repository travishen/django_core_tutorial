from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import PostModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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

    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('/blog/')

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


def post_model_update_view(request, id=None):
    post = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=post)
    context = {
        'form': form
    }
    if form.is_valid():
        f = form.save(commit=False)
        # modify form.attributes here...
        f.save()
        return HttpResponseRedirect('/blog/detail/{id}'.format(id=f.id))
    template = 'blog/update-view.html'

    return render(request, template, context)


def post_model_view(request, id=None):

    context = {}

    if id is not None:
        post = get_object_or_404(PostModel, id=id)
    else:
        post = None

    # view detail
    if 'detail' in request.get_full_path():

        # delete
        if request.method == 'POST':
            post.delete()
            return HttpResponseRedirect('/blog/')

        template = 'blog/detail/detail.html'
        context = {
            'post': post
        }

    # create / update
    if 'update' in request.get_full_path() or 'create' in request.get_full_path():
        if id is None:
            template = 'blog/create-view.html'
        else:
            template = 'blog/update-view.html'

        form = PostModelForm(request.POST or None, instance=post)
        context = {
            'form': form
        }
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return HttpResponseRedirect('/blog/detail/{id}'.format(id=f.id))

    # list
    if not context:
        template = 'blog/list-view.html'

        posts = PostModel.objects.all()
        queries = request.GET

        if queries.get('title'):
            title = queries.get('title')
            posts = posts.filter(
                Q(title__icontains=title) |
                Q(content__icontains=title)
            )

        context = {
            'posts': posts
        }

    return render(request, template, context)
