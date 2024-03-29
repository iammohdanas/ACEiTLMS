"""
URL configuration for ACEiT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .import views, user_login
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('base/',views.base,name='base'),
    
    path('',views.homepage,name="home"),
    
    # path('home/',views.homepage,name="home"),

    path('course/',views.single_course,name="single_course"),

    path("search",views.SEARCH_COURSE, name="search_course"),

    path('courses/filter-data',views.filter_data,name="filter-data"),

    path("404", views.PAGE_NOT_FOUND, name="404"),

    path('contact',views.contact_us,name="contact_us"),

    path('about',views.about_us,name="about_us"),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register',user_login.REGISTER,name='register'),

    path('doLogin',user_login.DO_LOGIN,name="doLogin"),

    path("accounts/profile", user_login.PROFILE,name='profile'),

    path("accounts/profile/update",user_login.PROFILE_UPDATE,name="profile_update"),

    path("course/<slug:slug>", views.COURSE_DETAILS, name="course_details")



] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
