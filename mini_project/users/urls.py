from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('store/', views.store_view, name='store'),

    # halaman khusus kategori
    path('karbu/', views.karbu_view, name='karbu'),  
    path('lampu/', views.lampu_view, name='lampu'),
    path('velg/', views.velg_view, name='velg'),
    path('blocksilinder/', views.blocksilinder_view, name='blocksilinder'),
    path('headsilinder/', views.headsilinder_view, name='headsilinder'),
    path('krukas/', views.krukas_view, name='krukas'),
    path('shock/', views.shock_view, name='shock'),

    path('checkout/<int:product_id>/', views.checkout_view, name='checkout'),
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path("orders/cancel/<int:order_id>/", views.cancel_order, name="cancel_order"),
    path('checkout/', views.checkout_view, name='checkout'),
]
