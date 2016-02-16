from __future__ import unicode_literals # must be at the top of a page

from django.db import models
from django.conf import settings
from django.utils.text import slugify #slugify turns our title into a slug

from django.db.models.signals import pre_save # right before the model is saved, we are going to do something
# from django.core.urlresolvers import reverse

def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s/%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    title = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug



# def pre_save_post_receiver(sender, instance, *args, **kwargs): # if this funciton is passed other things, go ahead and add them to args or kwargs
#     if not instance.slug:
#         instance.slug = create_slug(instance)


    # slug = slugify(instance.title)
    # # "tesla item 1" --> "tesla-item-1" == url ready
    # exists = Post.objects.filter(slug=slug).exists()
    # if exists:
    #     slug = "%s-%s" %(slug, instance.id)

    # instance.slug = slug


# def pre_save_connect(pre_save_post_receiver, sender=Post):


    # def get_absolute_url(self):
      # return reverse("posts:detail", kwargs={"id" : self.id})
      # return "/posts/%s/" %(self.id)


    # def get_absolute_url(self):
    #   return reverse("detail", kwargs={"id" : self.id})
    #   # return "/posts/%s/" %(self.id)
