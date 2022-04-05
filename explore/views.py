
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
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

temp = Charity.objects.all()


def search(request):
    query = request.POST['search']
    print("QUERY: ")
    print(query)
    #t = loader.get_template('explore.html')
    q = Charity.objects.filter(
        Q(name__icontains=query) | Q(charity_theme__icontains=query) | Q(
            location__icontains=query)
    )
    c = {'posts': q, }
    global temp
    temp = q
    #   return HttpResponse(t.render(c))
    return render(request, 'explore.html', c)


def explore_page(request):
    context = {
        'posts': Charity.objects.all()
        # 'posts' : posts
    }
    global temp
    temp = Charity.objects.all()
    return render(request, 'explore.html', context)


def detail(request, username):
    the_user = get_object_or_404(Charity, username=username)
    return render(request, 'Charity_HomePage.html', {'the_user': the_user, })
    # print(the_user)
    # return HttpResponse("<h2> Details for Charity id: " + str(username) + "</h2>")


def get_rating_sorted(request):
    context = {
        'posts': temp.order_by('-rating')
        # 'posts' : posts
    }
    print("helllpp")
    if request.method == "GET":
        return render(request, 'explore.html', context)


def get_AtoZ_sorted(request):
    context = {
        'posts': temp.order_by('name')
        # 'posts' : posts
    }
    if request.method == "GET":
        return render(request, 'explore.html', context)


def get_ZtoA_sorted(request):
    context = {
        'posts': temp.order_by('-name')
        # 'posts' : posts
    }
    if request.method == "GET":
        return render(request, 'explore.html', context)


def user_reg(request):
    return render(request, 'user_registration.html')


def charity_reg(request):
    return render(request, 'charity_registration.html')


def admin_approval(request):
    if request.method == "POST":
        organisation_name = request.POST['name']
        year = request.POST['year']
        location = request.POST['location']
        theme = request.POST['charity_theme']
        rating = request.POST['rating']
        pic_link = request.POST['pic_link']
        document = request.POST['certificate']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        passw = request.POST['password2']
        CharityInfo = Charity(name=organisation_name, year=year, location=location, charity_theme=theme, rating=rating,
                              pic_link=pic_link, certificate=document, username=username, email=email, password1=password, password2=passw)
        CharityInfo.save()
        return render(request, '/explore')


def admin_approval_view(request):
    registrations = Charity.objects.all()
    return render(request, 'adminapproval.html', {'registrations': registrations})


def Charity_approve_reg(request, charity_id):
    charity = Charity.objects.get(name=charity_id)
    charity.status = 1
    charity.save()
    return render(request, '/AdminApprovalView')


def Charity_disapprove_reg(request, charity_id):
    charity = Charity.objects.get(name=charity_id)
    charity.status = 2
    charity.save()
    return render(request, '/AdminApprovalView')
