from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'trafficking/index.html')

def chartPageView(request):
    return render(request,'trafficking/charts.html')