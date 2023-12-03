from django.shortcuts import render

from django.http import HttpResponse

def things_view(request):
    return render(request, 'things.html')    


# Create your views here.
