from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def members(request):
    return HttpResponse("Hello world!")
# Create your views here.
