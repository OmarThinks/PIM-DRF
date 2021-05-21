from django.db import models
from rest_framework import serializers

class Product(models.Model):
	product_code = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	price = models.FloatField()
	quantity = models.FloatField()


# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
