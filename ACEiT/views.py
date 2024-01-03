from django.shortcuts import render, redirect
from app.models import Categories
from app.models import Author
from app.models import Course
from app.models import Level


def base(request):
    return render(request,"base.html")


def homepage(request):
    category=Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('-id')

    context = {
        'category':category,
        'course': course
    }
    

    return render(request,"Main/home.html",context)

def single_course(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    context  = {
        'category': category,
        'level':level,
        'course':course,
    }
    print(course)
    return render(request,"Main/single_course.html",context)


def contact_us(request):
    return render(request,"Main/contact_us.html")

def about_us(request):
    return render(request,"Main/about_us.html")
    

