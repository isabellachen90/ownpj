from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def index(request):
    return render(request, 'hello/van.html')

def test(request):
    return render(request, 'hello/test.html')