"""
URL configuration for demoproject project.

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
# from demoapp import views  
from demoproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name= "index"), 
    path('', views.homePage,name='home'),
    path('about-us/', views.aboutUs,name='about'),
    path('products/', views.products,name='products'),
    path('contact-us/', views.contactus,name='contactus'),
    path('userform/', views.userForm,name='userform'),
    path('submitform/', views.submitform,name='submitform'),
    path('calculator/', views.calculator),
    path('saveevenodd/', views.saveevenodd),
    path('marksheet/', views.marksheet),
    path('course/', views.Course),
    path('newsdetails/<slug>', views.newsDetails),
    path('services/', views.service),
    # path('course/<int:courseid>', views.courseDetails),
    # path('course/<str:courseid>', views.courseDetails),
    # path('course/<slug:courseid>', views.courseDetails),
    path('course/<courseid>', views.courseDetails),
]
