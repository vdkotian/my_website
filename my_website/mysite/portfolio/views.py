from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
    print "Here it comes----------------"
    return render_to_response('portfolio/index.html')