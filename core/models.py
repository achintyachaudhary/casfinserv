from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=100)
    nse_code = models.CharField(max_length=100)
    bse_code = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.nse_code}'


class BTSTStock(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.DO_NOTHING)
    closing_price = models.DecimalField(decimal_places=2, max_digits=10)
    percentage_change = models.DecimalField(decimal_places=2, max_digits=10)
    volume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stock} {self.closing_price}'
