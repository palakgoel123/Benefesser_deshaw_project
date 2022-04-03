from msilib.schema import ListView
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Charity
from django.views.generic import TemplateView, ListView
from django.db.models import Q

posts = [
    {
        'name': 'Helping hands',
        'location': 'India',
        'charity_theme': 'education',
        'rating': 4.2,
        'pic_link': 'https://tourtelegraph.com/wp-content/uploads/2021/04/Anchorage_alaska.tourtelegraph-750x430.jpg'
    },
    {
        'name': 'xyz',
        'location': 'Africa',
        'charity_theme': 'food for everyone',
        'rating': 3.8,
        'pic_link': 'https://www.cbcity.nsw.gov.au/communityccb/PublishingImages/community/Youth/stay%20connected%20food.jpg'
    }
]

def search(request):
  query = request.POST['search']
  print( "QUERY: ")
  print(query)
  #t = loader.get_template('explore.html')
  q = Charity.objects.filter(
            Q(name__icontains=query) | Q(charity_theme__icontains=query) |  Q(location__icontains=query) 
        )
  c = { 'posts': q,}
#   return HttpResponse(t.render(c))
  return render(request, 'explore.html', c)


def explore_page(request):
    context = {
        'posts': Charity.objects.all()
        # 'posts' : posts
    }
    return render(request, 'explore.html', context)


def detail(request, charity_id):
    return HttpResponse("<h2> Details for Charity id: " + str(charity_id) + "</h2>")


def get_rating_sorted(request):
    context = {
        'posts': Charity.objects.all().order_by('-rating')
        # 'posts' : posts
    }
    print("helllpp")
    if request.method == "GET":
        return render(request, 'explore.html', context)


def get_AtoZ_sorted(request):
    context = {
        'posts': Charity.objects.all().order_by('name')
        # 'posts' : posts
    }
    if request.method == "GET":
        return render(request, 'explore.html', context)


def get_ZtoA_sorted(request):
    context = {
        'posts': Charity.objects.all().order_by('-name')
        # 'posts' : posts
    }
    if request.method == "GET":
        return render(request, 'explore.html', context)


def user_reg(request):
    return render(request, 'user_registration.html')


def charity_reg(request):
    return render(request, 'charity_registration.html')
