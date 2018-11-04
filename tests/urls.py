from django.conf.urls import include, url

from wagtail.core import urls

urlpatterns = [
  # Wagtail pages
  url(r'', include(urls)),
]