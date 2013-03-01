# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from app.forms import ClientForm

def home(request):
    form = ClientForm()
    return render_to_response('home.html', {'form':form }, context_instance=RequestContext(request))
