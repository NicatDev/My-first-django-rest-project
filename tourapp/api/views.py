from rest_framework.generics import RetrieveUpdateDestroyAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView,CreateAPIView,DestroyAPIView
from equipmentapp.paginations import CustomPagination
from rest_framework.mixins import RetrieveModelMixin
from tourapp.api.serializers import *
from tourapp.models import Favourite
from tourapp.api.permissions import IsOwnerorAdmin
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from tourapp.api.filters import *
from rest_framework.views import APIView
from rest_framework.response import Response


class DestinationListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CateogryFilter
    
class DestinationRetrieveView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset=Category.objects.all()
    lookup_field = "id"

class TourListView(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TourFilter
    serializer_class = TourSerializer
    pagination_class = CustomPagination
    queryset = Tour.objects.all()

"""
    def get_queryset(self, *args, **kvargs):
        request = self.request
        queryset = Tour.objects.all()
        category = request.GET.get("category", None)

        date = request.GET.get("date", None)
        search = request.GET.get("search", None)
        if category:
            queryset = queryset.filter(category__id=int(category))
       
        if type:
            queryset = queryset.filter(type__id=int(type))
        
        if date:
            queryset = queryset.filter(date__id=int(date))
        
        if search:
            queryset = queryset.filter(description=search)
        
            
        return queryset """
    
"""    def get_serializer_class(self):
        if self.request.method == "GET":
            return TourSerializer


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)"""


class FavouriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavouriteListCreateAPISerializer
    
    def get_queryset(self):
        return Favourite.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerorAdmin]
    

class TourListDetailView(generics.RetrieveAPIView):
    serializer_class = TourSerializer
    queryset=Tour.objects.all()
    lookup_field = "id"
    
class BookMarkView(APIView):
    
   def post(self, request):
        serializer = BookmarkSerializer(data=request.data)
        
        if serializer.is_valid():
            name = request.data.get('name')
            surname = request.data.get('surname')
            email = request.data.get('email')
            phone = request.data.get('phone')
            num_tickets = request.data.get('num_tickets')
            serializer.save()
            print('oke')
            send_mail(
                'Tur muracietiniz tesdiqlendi !',
                f'Hormetli {name} {surname} sizin turla bali muracietiniz AzKamp sirketi terefinden tesdiqlendi. Sizin ucun qeyd etdiyiiniz tura {num_tickets} bilet ayrilmisdir.Emekdaslarimiz tur tarixi yaxinlasdiqda {phone} nomresi ile elaqe saxlayacaq',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            print('okeee')
            return Response({'message':'success'})
        
        else:
            return Response({'error':serializer.errors})
        

class CategoryTourView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset=Category.objects.all()

class TypeTourView(generics.ListAPIView):
    serializer_class = TypeSerializer
    queryset=Type.objects.all()