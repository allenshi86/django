"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
from app01 import views as app01_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', app01_views.show,name='app01_views.show'),
    path('',app01_views.show,name='app01_views.show'),
]


'''
urlpatterns += [
    path('', RedirectView.as_view(url='/app01/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''