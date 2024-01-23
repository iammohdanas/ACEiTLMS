from django.shortcuts import render, redirect
from app.models import Categories
from app.models import Author
from app.models import Course
from app.models import Level
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from app.models import Video


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


def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course':course,
    }
    return render(request,'search/search.html',context)

def COURSE_DETAILS(request,slug):
    course = Course.objects.filter(slug=slug)
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum=Sum('time_duration'))

    if course.exists():
        course=course.first()
    else:
        return redirect('404')
    category = Categories.get_all_category(Categories)
    context = {
        'course':course,
        'category':category,
        'time_duration':time_duration,
    }
    return render(request,"course/course_details.html",context)

def single_course(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price = 0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()

    context  = {
        'category': category,
        'level':level,
        'course':course,
        'FreeCourse_count':FreeCourse_count,
        'PaidCourse_count':PaidCourse_count,
    }
    print(course)
    return render(request,"Main/single_course.html",context)

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    print(price)

    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
        Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in  = category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course':course
    }
    t = render_to_string('ajax/course.html',context)
    return JsonResponse({'data': t})



def contact_us(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request,"Main/contact_us.html",context)


def about_us(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request,"Main/about_us.html",context)

def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request,'error/404.html',context)

