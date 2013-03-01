# Create your views here.

from django.shortcuts import render_to_response ,redirect
from django.template import RequestContext
from app.forms import ClientForm
import urllib2
import urllib
import json


def home(request):
    if request.method=="POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            global client_id
	    global client_secret
	    client_id=request.POST['client_id']
	    client_secret=request.POST['client_secret']
	    return redirect('http://join.agiliq.com/oauth/authorize?client_id='+client_id+'&redirect_uri=http://127.0.0.1:8000/callback')
    else:
        form = ClientForm()
        return render_to_response('home.html', {'form':form }, context_instance=RequestContext(request))

def callback(request):
	code = request.GET['code']
	url = 'http://join.agiliq.com/oauth/access_token/'
	values = {'client_id' : client_id,
			  'redirect_uri' : 'http://localhost:8000/agiliq',
			  'client_secret' : client_secret,
			  'code': code,}


	req = urllib2.Request(url+urllib.urlencode(values))
	response = urllib2.urlopen(req)
	the_page = response.read()
	obj = json.loads(the_page)
	token=obj['access_token']
	return render_to_response('upload.html', {
	    'access_token': token,
	},)
