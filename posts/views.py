from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# get_object_or_404

from .models import Post

# def post_home(request): # handles the request, request comes in
#   return HttpResponse("<h1>Hello</h1>") # returning a response, there are many different types of responses


def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request, id=id): #id must match with the key word in the url, id and pk are best practices
    instance = get_object_or_404(Post, id=id) # get the instance, Post is the model
    # return HttpResponse("<h1>Detail</h1>")
    context = {
        "instance" : instance,
        "title" : instance.title,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "List",
    }
    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
