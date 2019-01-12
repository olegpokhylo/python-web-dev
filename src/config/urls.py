"""Root URL Configuration for Startup Organizer Project"""
from django.contrib import admin
from django.urls import include, path

from blog import urls as blog_urls
from organizer import urls as organizer_urls

api_urls = [
    path("", include(organizer_urls)),
    path("", include(blog_urls)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls)),
]
