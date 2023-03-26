from django.shortcuts import redirect, render
from .models import Category,Product
from django.contrib import messages

#Create your views here.
def collections(request):
    #Category = None
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "menuapp/collections.html", context)



def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category =Category.objects.filter(slug=slug).first()
        context = {'products': products , 'category' :category }
        return render (request, "menuapp/cindex.html", context)
    else:
        messages.warning (request, "No such category found")
        return redirect('collections')
    
def productview(request, cate_slug, prod_slug):    
    context = {}   
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter (slug=prod_slug, status=0)):
            products=Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
        else:
            messages.error(request, "No such product found")
           # return redirect('menu:collections')
    else:
        messages.error(request, "No such category found")
        #return redirect('menu:collections')
    return render (request, "menuapp/view.html",context)






def cart(request):
    return render(request,'menuapp/cart.html')