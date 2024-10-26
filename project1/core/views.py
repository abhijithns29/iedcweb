from django.shortcuts import render,redirect
from items.models import Category,items
# Create your views here.
from .form import signupForm
from django.contrib.auth import logout

def log_out(request):
    logout(request)
    item=items.objects.filter(is_sold=False)[0:6]
    Categories=Category.objects.all()

    return render(request,'core/index.html',{
        'categories':Categories,
        'items':item,
    })

def index(request):
    item=items.objects.filter(is_sold=False)[0:6]
    Categories=Category.objects.all()

    return render(request,'core/index.html',{
        'categories':Categories,
        'items':item,
    })

def contact(request):
    return render(request,'core/contact.html')


def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = signupForm
    return render(request,'core/signup.html',{
        'form':form
    })