from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello index.")
    context = RequestContext(request)
    context_dict = {'boldmessage':"I am bold font from the context"}
    return render_to_response("tango/index.html",context_dict,context)