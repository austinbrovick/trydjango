from __future__ import unicode_literals # must be at the top of a page

from django.db import models

from django.db.models.signals import pre_save
# from django.core.urlresolvers import reverse

def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s/%s" %(instance.id, instance.id, extension)
    return "%s/%s/%s" %(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title


# def pre_save_post_receiver(sender, instance, *args, **kwargs):


# def pre_save_connect(pre_save_post_receiver, sender=Post):


    # def get_absolute_url(self):
      # return reverse("posts:detail", kwargs={"id" : self.id})
      # return "/posts/%s/" %(self.id)


    # def get_absolute_url(self):
    #   return reverse("detail", kwargs={"id" : self.id})
    #   # return "/posts/%s/" %(self.id)
