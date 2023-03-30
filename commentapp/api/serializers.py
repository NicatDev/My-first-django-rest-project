from rest_framework.serializers import SerializerMethodField,ModelSerializer
from rest_framework import serializers
from commentapp.models import Comment,Blog,Category
from django.contrib.auth.models import User
from equipmentapp.models import Product
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id','email']
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','id','slug']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class BloggSerializer1(ModelSerializer):
    category = CategorySerializer()
    numberofcomments = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_numberofcomments(self,obj):
        return len(obj.comment.all())

class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content','rating','blog','user']

    def create(self,validate_data):
        blogid = validate_data.pop("blog")
        userid = validate_data.pop("user")
        comment = Comment.objects.create(blog=blogid,user=userid,**validate_data)
                #validate_data.blog = blogid
        comment.save()
        return comment

class TourCommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content','rating','tour','user']

    def create(self,validate_data):
        tourid = validate_data.pop("tour")
        userid = validate_data.pop("user")
        comment = Comment.objects.create(tour=tourid,user=userid,**validate_data)
                #validate_data.blog = blogid
        comment.save()
        return comment

class ProductCommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content','rating','product','user']

    def create(self,validate_data):
        productid = validate_data.pop("product")
        userid = validate_data.pop("user")
        comment = Comment.objects.create(product=productid,user=userid,**validate_data)
                #validate_data.blog = blogid
        comment.save()
        return comment
        

#Ic ice reply olmasi ucun yuxardaki childi yox get_repliesde self serializer istifade etdim.
class CommentListSerializer(ModelSerializer):

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



class BlogSerializer(ModelSerializer):
    comment = CommentListSerializer(many=True)
    category = CategorySerializer()
    numberofcomments = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = '__all__'

    def get_numberofcomments(self,obj):
        return len(obj.comment.all())
  
