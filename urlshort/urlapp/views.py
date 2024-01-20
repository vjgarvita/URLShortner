from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from .models import LinkInfo
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def add(request):
    if request.method=='POST':
        link=request.POST['link']
        link_id=str(uuid.uuid4())[:5]
        newlink=LinkInfo(link=link,link_id=link_id)
        newlink.save()
        return HttpResponse(link_id)
    
def shorten(request, pk):
    link_id = LinkInfo.objects.get(link_id = pk)
    return redirect(link_id.link)