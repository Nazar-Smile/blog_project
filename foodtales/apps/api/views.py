from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.generics import ListAPIView
from apps.api.serializers import ProductSerializer
from apps.shop.models import Product, ShopCategory
from apps.api.serializers import ShopCategorySerializer

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)
    permission_classes= [IsAuthenticated]
    
class ShopCategoryListAPIView(ListAPIView):
    serializer_class = ShopCategorySerializer
    queryset = ShopCategory.objects.all()
