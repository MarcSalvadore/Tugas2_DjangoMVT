from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_mywatchlist(request):
    data_watch_list = WatchList.objects.all()
    context = {
    'list_tontonan': data_watch_list,
    'nama': 'Marc Salvadore Silitonga',
    'NPM': '2106705543'
    }
    return render(request, "mywatchlist.html", context)
 
def watch_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_xml_id(request, id):
    dataId = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", dataId), content_type="application/xml")

def watch_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_id(request, id):
    dataId = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", dataId), content_type="application/json")

