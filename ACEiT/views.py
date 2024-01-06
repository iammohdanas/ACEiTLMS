from django.shortcuts import render, redirect
from app.models import Categories
from app.models import Author
from app.models import Course
from app.models import Level
from django.template.loader import render_to_string
from django.http import JsonResponse


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

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    if category:
        course = Course.objects.filter(category__id__in  = category).order_by('-id')
    elif level:
        level = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course':course
    }
    t = render_to_string('ajax/course.html',context)
    return JsonResponse({'data': t})



def contact_us(request):
    return render(request,"Main/contact_us.html")


def about_us(request):
    return render(request,"Main/about_us.html")
    

