from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def indexPageView(request):
    lstData = [
        {
            "date_missing": "10/30/2009",
            "last_name": "Sharmarice",
            "first_name": "Halima",
            "age_at_missing": "14",
            "city": "Granger",
            "state": "UT",
            "gender": "F",
            "race": "W"
        },

        {
            "date_missing": "10/16/2015",
            "last_name": "Martinez",
            "first_name": "Kimberly",
            "age_at_missing": "16",
            "city": "West Valley City",
            "state": "UT",
            "gender": "F",
            "race": "M"
        },

        {
            "date_missing": "07/23/2004",
            "last_name": "Gomez",
            "first_name": "Brenda",
            "age_at_missing": "3",
            "city": "Logan",
            "state": "UT",
            "gender": "F",
            "race": "H"
        },

        {
            "date_missing": "05/25/2003",
            "last_name": "Bishop",
            "first_name": "Acacia",
            "age_at_missing": "1",
            "city": "Salt Lake City",
            "state": "UT",
            "gender": "F",
            "race": "W"
        },

        {
            "date_missing": "08/03/2020",
            "last_name": "Salazar",
            "first_name": "Maria",
            "age_at_missing": "14",
            "city": "Snowville",
            "state": "UT",
            "gender": "F",
            "race": "H"
        },

        {
            "date_missing": "04/09/2020",
            "last_name": "Hernandez-Soto",
            "first_name": "Peggy",
            "age_at_missing": "6",
            "city": "Ogden",
            "state": "UT",
            "gender": "F",
            "race": "H"
        },

        {
            "date_missing": "06/24/2021",
            "last_name": "Jimenez",
            "first_name": "Lucero",
            "age_at_missing": "14",
            "city": "West Valley City",
            "state": "UT",
            "gender": "F",
            "race": "H"
        },

        {
            "date_missing": "11/08/2013",
            "last_name": "Colindres-Avila",
            "first_name": "Yuris",
            "age_at_missing": "17",
            "city": "West Valley City",
            "state": "UT",
            "gender": "F",
            "race": "M"
        },

        {
            "date_missing": "07/15/2021",
            "last_name": "Harris",
            "first_name": "Kandis",
            "age_at_missing": "16",
            "city": "Salt Lake City",
            "state": "UT",
            "gender": "F",
            "race": "W"
        },

        {
            "date_missing": "07/30/2006",
            "last_name": "Seal",
            "first_name": "Jaydan",
            "age_at_missing": "1",
            "city": "Garleys Wash",
            "state": "UT",
            "gender": "M",
            "race": "W"
        },

        {
            "date_missing": "06/13/2018",
            "last_name": "Lizarraga",
            "first_name": "Jose",
            "age_at_missing": "13",
            "city": "West Valley City",
            "state": "UT",
            "gender": "M",
            "race": "H"
        },

        {
            "date_missing": "04/23/2020",
            "last_name": "Cortez Trujillo",
            "first_name": "Eztli",
            "age_at_missing": "21",
            "city": "North Ogden",
            "state": "UT",
            "gender": "M",
            "race": "H"
        },

        {
            "date_missing": "10/25/2017",
            "last_name": "Fowles",
            "first_name": "Juan",
            "age_at_missing": "15",
            "city": "Lehi",
            "state": "UT",
            "gender": "M",
            "race": "M"
        },

        {
            "date_missing": "08/20/2012",
            "last_name": "Garcia",
            "first_name": "Isai",
            "age_at_missing": "17",
            "city": "West Valley City",
            "state": "UT",
            "gender": "M",
            "race": "M"
        },

        {
            "date_missing": "09/01/2015",
            "last_name": "Smith",
            "first_name": "Macin",
            "age_at_missing": "17",
            "city": "St. George",
            "state": "UT",
            "gender": "M",
            "race": "W"
        },

        {
            "date_missing": "01/26/2006",
            "last_name": "Sisco-Ramirez",
            "first_name": "Jose",
            "age_at_missing": "4",
            "city": "West Valley City",
            "state": "UT",
            "gender": "M",
            "race": "M"
        }
    ]

    context = {
        "data": lstData
    }

    return render(request, 'trafficking/index.html', context)


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
