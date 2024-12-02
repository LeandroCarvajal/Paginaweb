"""
URL configuration for tarot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from paginaweb import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),              # Página principal (home)
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
    path('floral/', views.floral, name='floral'),        # Página de terapia floral
    path('nosotros/', views.nosotros, name='nosotros'),  # Página "Nosotros"
    path('reiki/', views.reiki, name='reiki'),           # Página de Reiki
    path('resenas/', views.resenas, name='resenas'),     # Página de reseñas
    path('tienda/', views.tienda, name='tienda'),        # Página de la tienda
    path('tarot/', views.tarot, name='tarot'),           # Página de tarot
    path('login/', views.login, name='login'),  
    path('horas/', views.horas, name='horas'),  
    path('send-sms/', views.send_sms, name='send_sms'),
    path('post_mensaje/', views.post_mensaje, name='post_mensaje'),
]
