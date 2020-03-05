from django.urls import path
from django.contrib.auth import urls
from django.conf.urls import include

from django.views.generic.base import RedirectView

from . import views

urlpatterns = [

    path("templates/", views.templates, name="templates"),
    path("templates/<slug:slug>/", views.template, name="template"),
]
