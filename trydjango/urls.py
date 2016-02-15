from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# from posts import views
# url(r'^posts/$', views.post_home),
#REGEX = regular expressions


urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^posts/', include("posts.urls")), # there can't be a dollar sign after posts or else the pattern will stop
  # url(r'^posts/$', "<appname>.views.<function_name>"),

]


if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
