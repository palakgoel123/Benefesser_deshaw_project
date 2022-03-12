from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from . import views


# Code for video 7
urlpatterns = [
    path('explore/', views.explore_page, name='explore'),
    path('explore/sortedbyname_asc', views.get_AtoZ_sorted, name='bynameasc'),
    path('explore/sortedbyname_desc', views.get_ZtoA_sorted, name='bynamedesc'),
    path('explore/sortedbyrating', views.get_rating_sorted, name='byrating'),
    path('UserRegistration/', views.user_reg, name='user_reg_explore'),
    path('CharityRegistration/', views.charity_reg, name='charity_reg_explore'),
    #explore/ => charity/charity_id
    url(r'^charity/(?P<charity_id>[0-9A-Z]+)/$', views.detail, name='detailedpage' )
]