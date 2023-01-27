from rest_framework import serializers
from ..models import *

class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = "__all__"
    

                
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


        
class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    category = CategorySerializer()
    images = ProductImageSerializer(many=True)
    main_product_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_total_price(self, obj):
        discount_price = obj.discount_price if obj.discount_price else 0
        return obj.price + - discount_price
    
    def get_main_product_image(self,obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.main_product_image())
 
        
    
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "brand", "subcategory",
                  "price", "discount_price","chechstock","deleted",)
    
    def validate(self, attrs):
        name= attrs.get("name",None)
        if not name:
            raise serializers.ValidationError("Name is None")
        return attrs
        
        
    def create(self, validated_data):
        instance = Product.objects.create(
            **validated_data
        )
        return instance
    

class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
    
    def validate(self, attrs):
        return attrs
        
    def create(self, validated_data):
        instance = Basket.objects.create(
            **validated_data
        )
        return 
    
class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
        

class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
    
    def validate(self, attrs):
        return attrs
        
    def create(self, validated_data):
        instance = Basket.objects.create(
            **validated_data
        )
        return 