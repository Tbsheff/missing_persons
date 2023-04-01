from django.urls import path
from .views import indexPageView, chartPageView, aboutPageView, CTDCPageView, ToolkitPageView, HumanTraffickingHotlinePageView, UtahReportPageView, StatisticsPageView, UTAPageView, AttorneyGeneralPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("charts/", chartPageView, name="charts"),
    path("about/", aboutPageView, name="about"),
    path("CTDC/", CTDCPageView, name="CTDC"),
    path("toolkit/", ToolkitPageView, name="toolkit"),
    path("report/", UtahReportPageView, name="report"),
    path("hth/", HumanTraffickingHotlinePageView, name="hth"),
    path("stats/", StatisticsPageView, name="stats"),
    path("uta/", UTAPageView, name="UTA"),
    path("attorney/", AttorneyGeneralPageView, name="attorney"),
]
