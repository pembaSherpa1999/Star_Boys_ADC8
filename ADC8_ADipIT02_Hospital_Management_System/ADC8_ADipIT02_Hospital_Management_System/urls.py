"""ADC8_ADipIT02_Hospital_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

# this is the default django page
urlpatterns = [
    path('admin/', admin.site.urls),
]

# this is urls of Hospital application
urlpatterns += [
    path('', include('Hospital.urls')),
]

# this is the url for restapi application
urlpatterns += [
    path('api/', include('restapi.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
