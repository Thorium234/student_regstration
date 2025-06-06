"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from users import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',v.register,name="register"),
    path('',include('django.contrib.auth.urls')),
    path('',include('std_app.urls'))
]

admin.site.site_header='KIBU BIT REG FORM 2025'
admin.site.site_title='Details'
admin.site.index_title='admin area'
