from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# get_object_or_404

from django.core.urlresolvers import reverse

from .forms import PostForm # imports form
from .models import Post # imports Post schema

# def post_home(request): # handles the request, request comes in
#   return HttpResponse("<h1>Hello</h1>") # returning a response, there are many different types of responses


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None) #initialize it with parenthesis
    if form.is_valid(): # if all the fields are valid, do something amazing !
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully create")
        return HttpResponseRedirect(reverse("detail", kwargs={'id' : instance.id}))
    context = {
        "form" : form,
    }
    return render(request, "post_form.html", context)
    # return HttpResponse("<h1>Create</h1>")

def post_detail(request, id=id): #id must match with the key word in the url, id and pk are best practices
    instance = get_object_or_404(Post, id=id) # get the instance, Post is the model
    # return HttpResponse("<h1>Detail</h1>")
    context = {
        "instance" : instance,
        "title" : instance.title,
    }
    return render(request, "post_detail.html", context)



def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list" : queryset,
        "title" : "List",
    }
    return render(request, "post_list.html", context)




def listing(request):
    contact_list = Contacts.objects.all()


    return render(request, 'list.html', {'contacts': contacts})





def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id) # get the instance, Post is the model
    form = PostForm(request.POST or None, request.FILES or None, instance=instance) #initialize it with parenthesis
    if form.is_valid(): # if all the fields are valid, do something amazing !
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully saved")
        return HttpResponseRedirect(reverse("detail", kwargs={'id' : instance.id}))
    context = {
        "instance" : instance,
        "title" : instance.title,
        "form" : form,
    }
    return render(request, "post_form.html", context)






def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("list")



