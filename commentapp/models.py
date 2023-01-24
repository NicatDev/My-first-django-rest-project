from django.db import models
from django.db import models
from accountapp.utils import create_slug_shortcode
from equipmentapp.models import *
from django.contrib.auth.models import User


# Create your models here.
class Comment(BaseMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,related_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)   
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    
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
        
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def any_children(self):
        return Comment.objects.filter(parent = self).exists()