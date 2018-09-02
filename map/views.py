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
        'disease_year': 2017,
    }

    return render(request, 'home.html', context)

def tb_mortality(request):
    all_diseases = Disease.objects.filter(gho__iexact="TB_e_mort_exc_tbhiv_num", year__exact=2016).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
        'disease_name': get_disease_parameter("TB_e_mort_exc_tbhiv_num"),
        'disease_year': 2016,
    }

    return render(request, 'tb_mortality.html', context)


def tb_prevalence(request):
    all_diseases = Disease.objects.filter(gho__iexact="TB_e_prev_num", year__exact=2014).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
        'disease_name': get_disease_parameter("TB_e_prev_num"),
        'disease_year': 2014,
    }

    return render(request, 'tb_prevalence.html', context)


def menin_mortality(request):
    all_diseases = Disease.objects.filter(gho__iexact="MENING_1", year__exact=2014).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
        'disease_name': get_disease_parameter("MENING_1"),
        'disease_year': 2014,
    }

    return render(request, 'menin_mortality.html', context)


def menin_prevalence(request):
    all_diseases = Disease.objects.filter(gho__iexact="MENING_2", year__exact=2014).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
        'disease_name': get_disease_parameter("MENING_2"),
        'disease_year': 2014,
    }

    return render(request, 'menin_prevalence.html', context)


def cholera_mortality(request):
    all_diseases = Disease.objects.filter(gho__iexact="CHOLERA_0000000002", year__exact=2016).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
        'disease_name': get_disease_parameter("CHOLERA_0000000002"),
        'disease_year': 2016,
    }

    return render(request, 'cholera_mortality.html', context)


def cholera_prevalence(request):
    all_diseases = Disease.objects.filter(gho__iexact="CHOLERA_0000000001", year__exact=2016).values('country', 'numeric')

    altered_diseases = list(all_diseases)
    # print(altered_diseases)

    context = {
        'diseases': altered_diseases,
        'disease_name': get_disease_parameter("CHOLERA_0000000001"),
        'disease_year': 2016,
    }

    return render(request, 'cholera_prevalence.html', context)

# function to return disease parameter (ie name of disease statistic)
def get_disease_parameter(key):
    diseases_dict = {'HIV_0000000006': 'HIV Mortality Rate', 'TB_e_mort_exc_tbhiv_num': 'TB Mortality Rate',
                     'MENING_1': 'Meningitis mortality rate', 'CHOLERA_0000000002': 'Cholera Mortality Rate',
                     'CHOLERA_0000000001': 'Cholera Prevalence (Cases)', 'MENING_2': 'Meningitis Prevalence (Cases)',
                     'TB_e_prev_num': 'TB Prevalence Cases)'}
    name = diseases_dict[key]
    return name

