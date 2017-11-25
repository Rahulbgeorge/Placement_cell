from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def project_view(request):
    return render(request,"project_display.html")