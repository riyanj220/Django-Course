"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import home,contact
from vege.views import * 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home,name='home'), 
    path('receipes/',receipes,name='receipes'), 
    path('receipes/view_receipes/',view_receipes,name='view_receipes'), 
    path('receipes/delete_receipes/',delete_receipes,name='delete_receipes'), 
    path('receipes/update_receipes/',update_receipes,name='update_receipes'), 
    path('contact/',contact,name='contact'),   
    path('login_account/',login_account,name='login_account'),   
    path('logout_account/',logout_account,name='logout_account'),   
    path('register/',register,name='register'),   
    path('students/',get_student,name='get_student'),   
    path('see_marks/<student_id>/',see_marks,name='see_marks'),   
    path('admin/', admin.site.urls)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)