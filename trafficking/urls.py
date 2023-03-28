from django.urls import path
from .views import indexPageView, chartPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("charts/", chartPageView, name="charts"),
]
