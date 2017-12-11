from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import PostModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


@login_required()
def some_view(request):
    pass


def post_model_list_view(request):
    posts = PostModel.objects.all()
    # return HttpResponse(posts)
    template = 'blog/hello_world.html'
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
    pass