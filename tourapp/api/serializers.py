from rest_framework.serializers import SerializerMethodField,ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from tourapp.models import *
from commentapp.api.serializers import CommentListSerializer
from django.core.mail import send_mail
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        
class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = "__all__"

class TourSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    category = CategorySerializer()
    images = TourImageSerializer(many=True)
    main_product_image = serializers.SerializerMethodField()
    type = TypeSerializer()
    comment = CommentListSerializer(many=True)


    class Meta:
        model = Tour
        fields = "__all__"
    
    def get_total_price(self, obj):
        try:
            discount_price = obj.discount_price if obj.discount_price else 0
            return obj.price - discount_price
        except:
            return 'undefined'
    
    def get_main_product_image(self,obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.main_product_image())     
        
class TourAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = '__all__'       
        
        
class myTourSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    images = TourImageSerializer(many=True)
    main_product_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Tour
        fields = "__all__"

    def get_total_price(self, obj):
        try:
            discount_price = obj.discount_price if obj.discount_price else 0
            return obj.price - discount_price
        except:
            return 'undefined'
    
    def get_main_product_image(self,obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.main_product_image())


class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model=Favourite
        fields = '__all__'
        
        
    def validate(self, attrs):
        queryset = Favourite.objects.filter(tour = attrs['tour'],user = attrs['user'])
        if queryset.exists():
            raise serializers.ValidationError('Tekrar elave etmek mumkun deyil')
        return attrs

class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model=Favourite
        fields = ['content']
        
class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = TourMessages
        fields = '__all__'
    

        
    
  
