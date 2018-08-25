from django.shortcuts import render
from django.http import HttpResponse

from .models import Disease

# Create your views here.

def home(request):
    all_diseases = Disease.objects.filter(gho__iexact="HIV_0000000006", year__exact=2017).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
    }

    return render(request, 'home.html', context)

