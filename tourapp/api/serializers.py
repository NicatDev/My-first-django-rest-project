from rest_framework.serializers import SerializerMethodField,ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from tourapp.models import *

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


    class Meta:
        model = Tour
        fields = "__all__"

    def get_total_price(self, obj):
        discount_price = obj.discount_price if obj.discount_price else 0
        return obj.price - discount_price
    
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
        

  
