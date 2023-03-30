import django_filters
from commentapp.models import Blog

class BlogFilter(django_filters.FilterSet):
    category__id = django_filters.CharFilter(lookup_expr='iexact')
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
                                                                                    
    class Meta:
        model = Blog
        fields = ['category', "category__id", "category__name","name","description"]