# Create your views here.

from django.shortcuts import render_to_response ,redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from app.forms import ClientForm, ResumeUploadForm
import urllib, urllib2
import json, sys


def home(request):
    if request.method=="POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            global client_id
	    global client_secret
            global redirect_uri
            redirect_uri="http://127.0.0.1:8000/callback"
	    client_id=request.POST['client_id']
	    client_secret=request.POST['client_secret']
	    return redirect('http://join.agiliq.com/oauth/authorize?client_id='+client_id+'&redirect_uri='+redirect_uri, request_context=RequestContext(request))
    else:
        form = ClientForm()
        return render_to_response('home.html', {'form':form }, context_instance=RequestContext(request))


def callback(request):
	code = request.GET['code']
	url = 'http://join.agiliq.com/oauth/access_token/?'
	values = {'client_id' : client_id,
			  'redirect_uri' : redirect_uri,
			  'client_secret' : client_secret,
			  'code': code, }
	req = urllib2.Request(url+urllib.urlencode(values))
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	token=obj['access_token']
        form = ResumeUploadForm()
	return render_to_response('upload.html', {
	   'access_token': token, 'form':form,
	}, context_instance=RequestContext(request))
