from lib2to3.pgen2.token import MINEQUAL
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ProductForm
from .models import Product

# Show all products
@login_required(login_url='/login')
def products(request):
    if request.method == 'POST':
        search = request.POST['search']
        return render(request, 'products.html', {
            'products': Product.objects.filter(Q(name__icontains=search) | 
            Q(shade__icontains=search) | Q(brand__name__icontains=search))
        })        

    if request.GET.get('q') != None:
        q = request.GET.get('q') 
        return render(request, 'products.html', {
            'products': Product.objects.filter(brand__name__icontains=q)
        })
    else:
        return render(request, 'products.html', {
            'products': Product.objects.all()
        })

# Show single product page
@login_required(login_url='/login')
def product(request, id):
    return render(request, 'product.html', {
        'product': Product.objects.get(pk=id)
    })

# Add new product to database
@login_required(login_url='/login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'add.html',{
        'form': ProductForm()
    })

# Update/edit product info
@login_required(login_url='/login')
def update_product(request, id):
    product = Product.objects.get(pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
            # return redirect('product', product.id)

    return render(request, 'update.html', {
        'UpdateForm': ProductForm(instance=product)
    })            

# Delete product from database
@login_required(login_url='/login')
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            return render(request, 'login.html', {
                'message': 'Invalid Credentials'
            })

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')
    # return render(request, 'login.html', {
    #     'message': 'Successfully logged out'
    # })    