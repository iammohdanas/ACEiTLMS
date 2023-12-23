from django.shortcuts import render, redirect



def base(request):
    return render(request,"base.html")


def homepage(request):
    return render(request,"Main/home.html")

def single_course(request):
    return render(request,"Main/single_course.html")


def contact_us(request):
    return render(request,"Main/contact_us.html")

def about_us(request):
    return render(request,"Main/about_us.html")