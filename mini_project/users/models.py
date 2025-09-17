from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('velg', 'Velg'),
        ('karbu', 'Karbu'),
        ('lampu', 'Lampu'),
        ('blocksilinder', 'Blocksilinder'),
        ('headsilinder', 'Headsilinder'),
        ('krukas', 'Krukas'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='velg')

    def __str__(self):
        return f"{self.name} ({self.category})"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Selesai", "Selesai"),
        ("Dibatalkan", "Dibatalkan"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.status})"

# Model tambahan spesifik seperti Velg, Body, Lampu tetap bisa ada
class Velg(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to="velg_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Body(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to="body_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Lampu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to="lampu_images/", blank=True, null=True)

    def __str__(self):
        return self.name
