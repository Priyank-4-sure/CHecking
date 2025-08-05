from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserForm
from .models import Product
from django.shortcuts import get_object_or_404
from .models import Product, Order

def create_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        order = Order(
            user=request.user,
            product=product,
            shipping_address=request.POST.get('address'),
            phone=request.POST.get('phone')
        )
        order.save()
        return redirect('products')
    return render(request, 'store/order.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def load(request):
    return render(request,'store/index.html')

def loadl(request):
    return render(request,'store/location.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products')
    else:
        form = CustomUserForm()
    return render(request, 'store/signup.html', {'form': form})

