from rest_framework.serializers import SerializerMethodField,ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from tourapp.models import Favourite



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
        