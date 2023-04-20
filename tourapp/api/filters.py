import django_filters
from tourapp.models import *

class TourFilter(django_filters.FilterSet):
    category__id = django_filters.CharFilter(lookup_expr='iexact')
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    type__name = django_filters.CharFilter(lookup_expr='icontains')
    type__id = django_filters.CharFilter(lookup_expr='iexact')
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    date = django_filters.DateFilter()     
                           
    class Meta:
        model = Tour
        fields = ['category', "category__id",'type','type__id','type__name', "category__name","name","description",'date']
        
        
class CateogryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
       
    class Meta:
        model = Category
        fields = ['name']
      