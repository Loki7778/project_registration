from django.shortcuts import render

# Create your views here.
from  app.forms import *
from django.http import HttpResponse
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=='POST':
        TFO=TopicForm(request.POST)
        if TFO.is_valid():
            TFO.save()
            return HttpResponse('topic is inserted')
        else:
            return HttpResponse('it is not valid')


    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm
    d={'WFO':WFO}
    if request.method=='POST':
        WFO=WebpageForm(request.POST)
        
        if WFO.is_valid():
            WFO.save()
            return HttpResponse('webpage is inserted')
        else:
            return HttpResponse('it is not valid')

        
    return render(request,'insert_webpage.html',d)