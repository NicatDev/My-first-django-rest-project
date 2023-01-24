from django.db import models
from django.contrib.auth import get_user_model
from accountapp.utils import create_slug_shortcode
from django.contrib.auth.models import User
# Create your models here.



class BaseMixin(models.Model):
    slug = models.SlugField(unique=True, editable=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        abstract = True


class Category(BaseMixin):
    name = models.CharField(max_length=300)
    description = models.TextField(verbose_name="Zona haqqinda")

    def __str__(self):
        return self.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Zona"
        verbose_name_plural = "Zonalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Category)

        super(Category, self).save(*args, **kwargs)



class Type(BaseMixin):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="media/type")
    
    def __str__(self):
        return self.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Erazi"
        verbose_name_plural = "Eraziler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Type)

        super(Type, self).save(*args, **kwargs)


class Tour(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300,verbose_name="title")
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(verbose_name="Tur tarixi")
    # price fields
    price = models.FloatField()
    email = models.EmailField(verbose_name="mail")
    image = models.ImageField(upload_to="media/tour",)
    

    # is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Tour"
        verbose_name_plural = "Tours"

    def main_product_image(self):
        product_images = ZoneImage.objects.filter(product=self)
        if product_images.exists():
            return product_images.first().image.url
        return "-"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Tour)

        super(Tour, self).save(*args, **kwargs)


def upload_to(instance, filename):
    return "%s/%s/%s" % ("category", instance.product.name, filename)


class ZoneImage(BaseMixin):
    zona = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.product.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Tour Image"
        verbose_name_plural = "Tour Images"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=ZoneImage)

        super(ZoneImage, self).save(*args, **kwargs)

class Favourite(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    content = models.CharField(max_length=120)
    
    def __str__(self):
        return self.user.username
    
 