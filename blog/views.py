from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Post, Comment

import re
from datetime import datetime
from django.http import HttpResponse


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_hello(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using
    # regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                # mc added
                slider_val=form.cleaned_data["slider_val"],
                post=post,
            )
            comment.save()
    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)
