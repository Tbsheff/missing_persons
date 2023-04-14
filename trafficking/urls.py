from django.urls import path
from .views import indexPageView, chartPageView, aboutPageView, CTDCPageView, ToolkitPageView, HumanTraffickingHotlinePageView, UtahReportPageView, StatisticsPageView, UTAPageView, AttorneyGeneralPageView, showPersonPageView, displayPersonPageView

urlpatterns = [

    path("<int:id>/", displayPersonPageView, name="displayPerson"),
    path("showPerson/", showPersonPageView, name="showPerson"),
    path("charts/", chartPageView, name="charts"),
    path("about/", aboutPageView, name="about"),
    path("CTDC/", CTDCPageView, name="CTDC"),
    path("toolkit/", ToolkitPageView, name="toolkit"),
    path("report/", UtahReportPageView, name="report"),
    path("hth/", HumanTraffickingHotlinePageView, name="hth"),
    path("stats/", StatisticsPageView, name="stats"),
    path("uta/", UTAPageView, name="UTA"),
    path("attorney/", AttorneyGeneralPageView, name="attorney"),
    path("", indexPageView, name="index"),

]
