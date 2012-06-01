from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

def viewlog(request):
    return render_to_response('graph.html')

def data(request):
    json_data = json.dumps({'data':'[10,8,5,7,4,4,1]'})
    return HttpResponse(json_data)
