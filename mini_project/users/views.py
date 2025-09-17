from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from django.contrib import messages


def home_view(request):
    if request.user.is_authenticated:
        products = Product.objects.all()[:8] 
        # return redirect('store')  # langsung ke store kalau sudah login
    return render(request, 'users/home.html' , {"products": products})# kalau belum, tetap ke home


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # cek apakah user sudah ada
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah terdaftar!")
            return redirect('register')

        # buat user baru
        user = User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "Registrasi berhasil! Silakan login.")
        return redirect('login')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # cek email atau username
        try:
            user_obj = User.objects.get(email=username_or_email)
            username = user_obj.username
        except User.DoesNotExist:
            username = username_or_email

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')  # langsung ke store setelah login
        else:
            return render(request, 'users/login.html', {
                'error': 'Username/email atau password salah.'
            })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def store_view(request):
    products = Product.objects.all()
    return render(request, 'users/store.html', {
        'products': products,
        'is_authenticated': request.user.is_authenticated
    })


def checkout_view(request, product_id):
    if not request.user.is_authenticated:
        # kalau belum login, kasih alert lalu redirect ke login
        messages.error(request, "Harus register & login terlebih dahulu untuk checkout!")
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.create(
        user=request.user,
        product=product,
        status="Pending"   # status default
    )
    messages.success(request, f"Pesanan {product.name} berhasil dibuat!")
    return redirect('store')


@login_required
def my_orders_view(request):
    # gunakan select_related supaya query lebih efisien
    orders = Order.objects.filter(user=request.user).select_related('product').order_by('-created_at')
    return render(request, 'users/my_orders.html', {'orders': orders})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).select_related('product').order_by('-created_at')
    return render(request, "my_orders.html", {"orders": orders})


@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status.lower() == "pending":  # hanya bisa dibatalkan kalau statusnya Pending
        order.status = "Dibatalkan"
        order.save()
        messages.success(request, f"Pesanan {order.product.name} berhasil dibatalkan.")
    else:
        messages.warning(request, "Pesanan sudah tidak bisa dibatalkan.")
    return redirect("my_orders")


def velg_view(request):
    velgs = Product.objects.filter(category='velg')
    return render(request, 'users/velg.html', {
        'velgs': velgs,
        'is_authenticated': request.user.is_authenticated
    })

def karbu_view(request):
    # Filter produk dengan kategori 'karbu'
    products = Product.objects.filter(category='karbu')
    return render(request, 'users/karbu.html', {
        'products': products,
        'is_authenticated': request.user.is_authenticated
    })

def lampu_view(request):
    products = Product.objects.filter(category='lampu')
    return render(request, 'users/lampu.html', {
        'products': products,
        'is_authenticated': request.user.is_authenticated
    })

def blocksilinder_view(request):
    products = Product.objects.filter(category='blocksilinder')
    return render(request, 'users/blocksilinder.html', {
        'products': products,
        'is_authenticated': request.user.is_authenticated
    })
    
def headsilinder_view(request):
    products = Product.objects.filter(category='headsilinder')
    return render(request, 'users/headsilinder.html', {
        'products': products,
        'is_authenticated': request.user.is_authenticated
    })
    
def krukas_view(request):
    products = Product.objects.filter(category='krukas')
    return render(request, 'users/krukas.html', {
        'products': products,
        'is_authenticated': request.user.is_authenticated
    })
