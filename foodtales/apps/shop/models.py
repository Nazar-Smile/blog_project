from django.db import models

# Create your models here.

class ShopCategory(models.Model):
    name = models.CharField("название", max_length = 50)
    slug = models.SlugField(max_length = 70)

    class Meta:
        verbose_name = "категория товара"
        verbose_name_plural = "категории товара"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("название", max_length = 255)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits = 10, decimal_places =2)
    category = models.ForeignKey(ShopCategory, on_delete =models.SET_NULL, null = True, related_name = "products")
    is_available = models.BooleanField("доступно", default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    main_image = models.ImageField(upload_to="product/mains", null=True)



    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["-created"]
    

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete = models.CASCADE, 
        related_name = "images"
    )
    image= models.ImageField(upload_to = "prducts/images")

    def __str__(self):
        return self.product.name