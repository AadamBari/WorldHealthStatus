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
        'disease_name': get_disease_parameter("HIV_0000000006"),
    }

    return render(request, 'home.html', context)


# function to return disease parameter (ie name of disease statistic)
def get_disease_parameter(key):
    diseases_dict = {'HIV_0000000006': 'HIV Fatality Rate'}
    name = diseases_dict[key]
    return name

