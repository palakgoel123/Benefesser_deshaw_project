import string
from django.contrib import admin
from django.urls import include, re_path
from django.urls import include, path
from . import views


# Code for video 7
urlpatterns = [
    re_path(r'^test_search_results/$', views.search, name='search'),
    # //re_path(r'^search', views.SearchResultsView.as_view(), name='search_results'),
    path('explore/', views.explore_page, name='explore'),
    re_path(r'^sortedbyname_asc/', views.get_AtoZ_sorted, name='bynameasc'),
    # path('explore/sortedbyname_asc/', views.get_AtoZ_sorted, name='bynameasc'),

    re_path(r'^sortedbyname_desc/', views.get_ZtoA_sorted, name='bynamedesc'),
    re_path(r'^sortedbyrating/', views.get_rating_sorted, name='byrating'),
    path('/UserRegistration/', views.user_reg, name='user_reg_explore'),
    path('/CharityRegistration/', views.charity_reg, name='charity_reg_explore'),
    # explore/ => charity/charity_id
    re_path(r'^charity/(?P<username>\w+)/$',
            views.detail, name='detailedpage'),
    path('AdminApproval/', views.admin_approval, name='admin_approval'),
    path('AdminApprovalView/', views.admin_approval_view,
         name='admin_approval_view'),
    path('Charity_approve_reg/<str:charity_id>',
         views.Charity_approve_reg, name='Charity_approve_reg'),
    path('Charity_disapprove_reg/<str:charity_id>',
         views.Charity_disapprove_reg, name='Charity_disapprove_reg')

]
