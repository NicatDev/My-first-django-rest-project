from urllib import request
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from equipmentapp.models import Product,Category, User,ProductImage
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from equipmentapp.paginations import CustomPagination
from equipmentapp.api.permissions import IsOwnerorAdmin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = CustomPagination
    

    def get_queryset(self, *args, **kvargs):
        request = self.request
        queryset = Product.objects.all()
        category = request.GET.get("category", None)
        search = request.GET.get("search", None)
        if category:
            queryset = queryset.filter(subcategory__category__id=int(category))
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializer
        return ProductCreateSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

#detailview
class ProductRetrieveView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

#imageview
"""class ImageView(generics.ListAPIView):
    serializer_class = ProductImageSerializer
    qeuryset = ProductImage.objects.all()

    def get_queryset(self, *args, **kvargs):
        request = self.request
        queryset = ProductImage.objects.all()
        return queryset"""


#createupdatedeleteproduct
""""
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsOwnerorAdmin] 

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    
    def post(self, request,*args,**kvargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_product = serializer.save(user=self.request.user)
        return Response(serializer.data,status=201)
        

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerorAdmin] 

    def put(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.serializer_class(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerorAdmin] 
    
"""
    
    
class addbasketview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketCreateSerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerorAdmin]
    
    
    
    def get_queryset(self, *args, **kvargs):
        request = self.request
        queryset = Basket.objects.filter(user=request.user)
        return queryset


class BasketListView(generics.ListCreateAPIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self, *args, **kvargs):
        request = self.request
        queryset = Basket.objects.filter(user=request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

