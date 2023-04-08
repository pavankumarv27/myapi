from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self) -> str:
        return self.title