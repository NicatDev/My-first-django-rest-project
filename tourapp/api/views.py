from rest_framework.generics import RetrieveUpdateDestroyAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView,CreateAPIView,DestroyAPIView
from equipmentapp.paginations import CustomPagination
from rest_framework.mixins import RetrieveModelMixin
from tourapp.api.serializers import FavouriteAPISerializer,FavouriteListCreateAPISerializer
from tourapp.models import Favourite
from tourapp.api.permissions import IsOwnerorAdmin



class FavouriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavouriteListCreateAPISerializer
    
    def get_queryset(self):
        return Favourite.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    
class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerorAdmin]
    
    