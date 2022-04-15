from django.shortcuts import render
from .models import balance
# Create your views here.
def profile_page(request):
    context = {
        'posts': balance.objects.all().filter(user=request.user),
        # 'posts' : posts
    }
    # user = balance.objects.get(user=request.user)
    try:
        user =  balance.objects.get(user=request.user)
    except balance.DoesNotExist:
        user = None
    if user is not None:
        return render(request, 'user_page.html',{"balance":user.balance})
    else:
        return render(request, 'user_page.html')


def addmoney(request):
    context = {
        'posts': balance.objects.all().filter(user=request.user),
        # 'posts' : posts
    }
    
    return render(request, 'add_money.html',context)

def adding(request):
    query = request.POST.get('adding', False)
    print( "QUERY: ")
    print(query)
    #t = loader.get_template('explore.html')
    
    t = balance.objects.all().filter(user=request.user)
    for tt in t:
        print(tt)
        tt.balance += int(query)  # change field
        tt.save() # this will update only

    #   return HttpResponse(t.render(c))
    return profile_page(request)