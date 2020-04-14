from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index1(request):
    return render(request, "openpage.html")

def index2(request):
    if request.method == "POST":
        form = contact(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = contact()
        return render(request,"contact.html",{'form':form})