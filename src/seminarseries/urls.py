from django.urls import path
from . import views
from ie.urls_baseline import baseline_urlpatterns

urlpatterns = baseline_urlpatterns + [
    path("", views.index, name="index"),
]
