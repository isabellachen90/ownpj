from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'testapp/index.html',{})

def firstpage(request):
    return render(request, 'testapp/firstpage.html',{})

def secpage(request):
    return render(request, 'testapp/secpage.html', {})

def thirdpage(request):
    return render(request, 'testapp/thirdpage.html',{})

def lastpage(request):
    return render(request, 'testapp/lastpage.html')