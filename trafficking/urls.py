from django.urls import path
from .views import indexPageView, chartPageView, aboutPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("charts/", chartPageView, name="charts"),
    path("about/", aboutPageView, name="about"),
]
