from django.shortcuts import render,get_object_or_404


from django.contrib.auth.decorators import login_required
from items.models import items,Category

# Create your views here.


@login_required
def index(request):
    item = items.objects.filter(created_by=request.user)
    Categories =Category.objects.all()
    return render(request,'dashboard/index.html',{
        'items':item,
        'categories':Categories,
    })
