from django.core.management.base import BaseCommand
from users.models import Product


class Command(BaseCommand):
    help = "Seed initial data for Product model"

    def handle(self, *args, **kwargs):
        products = [
            {"name": "Velg Racing 17 Inch", "description": "Velg racing keren untuk motor/mobil", "price": 2500000, "category": "velg"},
            {"name": "Velg Standar 14 Inch", "description": "Velg standar untuk city car", "price": 1200000, "category": "velg"},
            {"name": "Bodykit Sport", "description": "Bodykit sporty untuk sedan", "price": 3500000, "category": "body"},
            {"name": "Bodykit Offroad", "description": "Bodykit tangguh untuk SUV", "price": 4000000, "category": "body"},
            {"name": "Lampu LED Headlight", "description": "Lampu LED terang dan hemat energi", "price": 800000, "category": "lampu"},
            {"name": "Lampu Foglamp", "description": "Lampu kabut untuk visibilitas malam hari", "price": 500000, "category": "lampu"},
        ]

        for p in products:
            Product.objects.get_or_create(
                name=p["name"],
                defaults={
                    "description": p["description"],
                    "price": p["price"],
                    "category": p["category"]
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ Seed data berhasil dimasukkan!"))
