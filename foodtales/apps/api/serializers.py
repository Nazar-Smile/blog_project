from apps.shop.models import Product, ShopCategory
from rest_framework import serializers


class ShopCategorySerializer(serializers.ModelSerializer):
    model = ShopCategory
    fields = "__alt__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__alt__"


