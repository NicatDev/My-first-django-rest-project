from rest_framework.generics import RetrieveAPIView,UpdateAPIView,ListAPIView,CreateAPIView,DestroyAPIView
from commentapp.api.serializers import *
from commentapp.models import Comment
from commentapp.api.permissions import IsOwnerorAdmin
from equipmentapp.paginations import CustomPagination
from rest_framework.mixins import RetrieveModelMixin



class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    
class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(product = query)
        return queryset


#retrievemodelmixin destroyapiview-a get ozelliyi verir
class CommentDeleteAPIView(DestroyAPIView,RetrieveModelMixin):
    serializer_class = CommentDeleteUpdateSerializer
    queryset = Comment.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsOwnerorAdmin]  
    #model mixin ucun get funksiyasi
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  
    
    
    
    
class CommentUpdateAPIView(UpdateAPIView,RetrieveModelMixin):
    serializer_class = CommentDeleteUpdateSerializer
    queryset = Comment.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsOwnerorAdmin]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  