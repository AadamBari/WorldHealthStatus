from django.shortcuts import render
from django.http import HttpResponse

from .models import DiseaseType

# Create your views here.

def home(request):
    all_diseases = DiseaseType.objects.all()

    context = {
        'diseases': all_diseases,
    }

    return render(request, 'home.html', context)

