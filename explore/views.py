from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from .models import Charity

# posts = [
#     {
#         'name': 'abc',
#         'location': 'Alaska',
#         'charity_theme': 'education',
#         'rating': 4.2,
#         'pic_link': 'https://tourtelegraph.com/wp-content/uploads/2021/04/Anchorage_alaska.tourtelegraph-750x430.jpg'
#     },
#     {
#         'name': 'xyz',
#         'location': 'Africa',
#         'charity_theme': 'food for everyone',
#         'rating': 3.8,
#         'pic_link': 'https://www.cbcity.nsw.gov.au/communityccb/PublishingImages/community/Youth/stay%20connected%20food.jpg'
#     }
# ]

def explore_page(request):
    context={
        'posts': Charity.objects.all()
    }
    return render(request,'explore.html',context)

def detail(request,charity_id):
    return HttpResponse("<h2> Details for Charity id: " + str(charity_id)+"</h2>")


def get_rating_sorted(request):
    context={
        'posts': Charity.objects.all().order_by('-rating')
    }
    print("helllpp")
    if request.method == "GET":
        return render(request, 'explore.html',context)

def get_AtoZ_sorted(request):
    context={
        'posts': Charity.objects.all().order_by('name')
    }
    if request.method == "GET":
        return render(request,'explore.html',context)

def get_ZtoA_sorted(request):
    context={
        'posts': Charity.objects.all().order_by('-name')
    }
    if request.method == "GET":
        return render(request,'explore.html',context)

def user_reg(request):
    return render(request, 'user_registration.html')


def charity_reg(request):
    return render(request, 'charity_registration.html')