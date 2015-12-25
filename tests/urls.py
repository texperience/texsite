from django.conf.urls import include, url

from wagtail.wagtailcore import urls

urlpatterns = [
  # Wagtail pages
  url(r'', include(urls)),
]