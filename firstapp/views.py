from django.shortcuts import render

from .models import Profile

# Create your views here.

def homepage(request):
    contex={
      'profile':Profile.objects.all()
    }

    return render(request,'index.html',contex)
