"""world_health_status URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# New to Django 2.0
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from map import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tb_mortality', views.tb_mortality, name='tb_mortality'),
    path('menin_mortality', views.menin_mortality, name='menin_mortality'),
    path('menin_prevalence', views.menin_prevalence, name='menin_prevalence'),
    path('cholera_mortality', views.cholera_mortality, name='cholera_mortality'),
    path('cholera_prevalence', views.cholera_prevalence, name='cholera_prevalence'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


