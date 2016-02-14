from django.contrib import admin

from .models import Post # relative import

class PostModelAdmin(admin.ModelAdmin):
  list_display = ["__unicode__", "updated", "timestamp"] #shows timestamp fields
  list_display_links = ["updated"]
  list_filter = ["updated", "timestamp"] #how do you want to filter on admin site?
  search_fields = ['title', 'content']
  class Meta:
    model = Post





admin.site.register(Post, PostModelAdmin) # built in admin function
