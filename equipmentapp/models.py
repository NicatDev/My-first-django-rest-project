from django.db import models
from django.contrib.auth import get_user_model
from accountapp.utils import create_slug_shortcode
from tourapp.models import *

# Create your models here.

User = get_user_model()


class BaseMixin(models.Model):
    slug = models.SlugField(unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseMixin):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Category)

        super(Category, self).save(*args, **kwargs)




class Product(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    chechstock = models.BooleanField(verbose_name="stokda var")
    deleted = models.BooleanField(default=False)
    
    # price fields
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    
    

    def __str__(self):
        return self.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def main_product_image(self):
        product_images = ProductImage.objects.filter(product=self)
        if product_images.exists():
            return product_images.first().image.url
        return "-"

    def total_price(self):
        discount_price = self.discount_price if self.discount_price else 0
        return self.price - discount_price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Product)

        super(Product, self).save(*args, **kwargs)





def upload_to(instance, filename):
    return "%s/%s/%s" % ("products", instance.product.name, filename)


class ProductImage(BaseMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.product.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=ProductImage)

        super(ProductImage, self).save(*args, **kwargs)



class Basket(BaseMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ("-id",)
        verbose_name = "Basket"
        verbose_name_plural = "Basket"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Basket)

        super(Basket, self).save(*args, **kwargs)
