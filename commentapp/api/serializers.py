from rest_framework.serializers import SerializerMethodField,ModelSerializer
from rest_framework import serializers
from commentapp.models import Comment,Blog
from django.contrib.auth.models import User
from equipmentapp.models import Product


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_at','updated_at',]
        
    def validate(self, attrs):
        if (attrs['parent']):
            if attrs['parent'].product != attrs['product']:
                raise serializers.ValidationError("Comment-Post elaqesi duzgun qurulmayib - by admin")
        return attrs
    

class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id','email']
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','id','slug']
        

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

#Ic ice reply olmasi ucun yuxardaki childi yox get_repliesde self serializer istifade etdim.
class CommentListSerializer(ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        #depth = 1 foreignkeyle baglanan modellerin butun fieldlerin getirdiyi ucun basqa metod istifade etdim
    



class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'content',
        )