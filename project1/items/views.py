from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404,redirect
from .models import items,Category
from .forms import NewitemForm,EdititemForm


def item(request):
    item= items.objects.filter(is_sold=False)
    query = request.GET.get('query','')
    category_id = request.GET.get('category', 0)
    Categories = Category.objects.all()

    if category_id:
        item = item.filter(category_id=category_id)

    if query:
        item=item.filter(Q(name__icontains=query) | Q(decription__icontains=query))

    return render(request,'item/item.html',{
        'items':item,
        'query':query,
        'categories':Categories,
        'category_id': int(category_id),
    })






# Create your views here.
def detail(request, pk):
    # Get the specific item
    item = get_object_or_404(items, pk=pk)
    # Use the item's category to filter related items
    related_items = items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method=='POST':
        form = NewitemForm(request.POST,request.FILES)


        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = NewitemForm()

    return render(request,'item/new.html',{
        'form':form,
        'title':'ADD item',

    })

@login_required
def edit(request,pk):
    item = get_object_or_404(items, pk=pk,created_by=request.user)
    if request.method=='POST':
        form = EdititemForm(request.POST,request.FILES,instance=item)


        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = EdititemForm(instance=item)

    return render(request,'item/new.html',{
        'form':form,
        'title':'Edit item',

    })


@login_required
def delete(request, pk):
    # Get the specific item
    item = get_object_or_404(items, pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')



