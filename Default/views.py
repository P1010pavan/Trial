from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index1(request):
    return render(request, "openpage.html")

