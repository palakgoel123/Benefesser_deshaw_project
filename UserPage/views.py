from django.shortcuts import render
from .models import balance
# Create your views here.
def profile_page(request):
    context = {
        'posts': balance.objects.all().filter(user=request.user),
        # 'posts' : posts
    }
    user = balance.objects.get(user=request.user)
    return render(request, 'user_page.html',{"balance":user.balance})

def addmoney(request):
    context = {
        'posts': balance.objects.all().filter(user=request.user),
        # 'posts' : posts
    }
    
    return render(request, 'add_money.html',context)