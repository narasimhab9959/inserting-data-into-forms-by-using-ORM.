from django.shortcuts import render
from app.models import *
from django.db.models.functions import *
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic_name is cretaed ')
    return render(request,'insert_topic.html')

def insert_Webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':

        tn=request.POST['tn']
        print(tn)
        name=request.POST['wn']
        url=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        print(TO)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('data is created in webpage')

    return render(request,'insert_Webpage.html',d)