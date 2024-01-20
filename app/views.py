from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TFO=Topic_form()
    d={'TFO':TFO}
    if request.method=='POST':
        TFDO=Topic_form(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    WFO=Webpage_form()
    d={'WFO':WFO}
    if request.method=='POST':
        WFDO=Webpage_form(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_webpage.html',d)
def insert_access(request):
    AFO=Access_form()
    d={'AFO':AFO}
    if request.method=='POST':
        AFDO=Access_form(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse("data is inserted")
    return render(request,'insert_access.html',d)