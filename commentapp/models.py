from django.db import models
from django.db import models
from accountapp.utils import create_slug_shortcode
from equipmentapp.models import *
from django.contrib.auth.models import User



class Blog(BaseMixin):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blogimage/')

    
    def __str__(self):
        return self.name or self.slug

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Blog "
        verbose_name_plural = "Blogs"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Blog)

        super(Blog, self).save(*args, **kwargs)



# Create your models here.
class Comment(BaseMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,related_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)   

    
    def __str__(self):
        return self.product.name + ' - ' + self.user.username + ' - ' + self.content[0:10]

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Commentler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug_shortcode(size=12, model_=Comment)

        super(Comment, self).save(*args, **kwargs)
        
