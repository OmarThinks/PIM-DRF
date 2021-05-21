from django.db import models

class Product(models.Model):
	product_code = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	price = models.FloatField()
	quantity = models.FloatField()