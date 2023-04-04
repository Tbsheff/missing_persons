from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def indexPageView(request):
    return render(request, 'trafficking/index.html')


def chartPageView(request):
    return render(request, 'trafficking/charts.html')


def aboutPageView(request):
    return render(request, 'trafficking/about.html')


def CTDCPageView(request):
    return redirect('https://www.ctdatacollaborative.org/story/age-victims-children-and-adults')


def ToolkitPageView(request):
    return redirect('https://sharedhope.org/PICframe7/analysis/PIC_AR_2017_UT.pdf')


def UtahReportPageView(request):
    return redirect('https://sharedhope.org/PICframe7/reportcards/PIC_RC_2017_UT.pdf')


def HumanTraffickingHotlinePageView(request):
    return redirect('https://humantraffickinghotline.org/en/statistics/utah')


def StatisticsPageView(request):
    return redirect('https://www.acf.hhs.gov/sites/default/files/documents/otip/utah_profile_efforts_to_combat_human_trafficking.pdf')


def UTAPageView(request):
    return redirect('https://www.rideuta.com/news/2021/01/Human-Trafficking')


def AttorneyGeneralPageView(request):
    return redirect('https://attorneygeneral.utah.gov/initiatives/human-trafficking/')
