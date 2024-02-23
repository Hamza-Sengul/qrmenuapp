from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category/', blank=True, null=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Fiyat alanı
    description = models.TextField(blank=True, null=True)  # Açıklama alanı (Rich Text)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Resim alanı
    service_duration = models.CharField(max_length=100, blank=True, null=True)  # Servis süresi alanı

    def __str__(self):
        return self.name


class Call(models.Model):
    table_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Masa {self.table_number} - {self.timestamp}"

