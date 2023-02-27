from django.urls import path
from  apps.cart import views


urlpatterns = [
    path('', views.CartView.as_view(), name="cart_page"), 
    path('add/<int:product_id>/', views.AddCartView.as_view(), name="add_cart"), 
    path('delete/<int:product_id>/', views.DeleteProductCartView.as_view(), name= "delete_cart"), 
    path('clear/', views.ClearCartView.as_view(), name= "clear_cart")

]