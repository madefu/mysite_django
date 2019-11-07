from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def hello(request):
    context          = {"madefu":'madefu'}
    return render(request, 'hello.html', context)

def index(request):
	return HttpResponse("This is a test page")
