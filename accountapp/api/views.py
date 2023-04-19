from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from accountapp.api.serializers import *
from django.contrib.auth import get_user_model, login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
User = get_user_model()

class CheckPost(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        return Response({"success": True})
        
class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.data.get("username")
        password = serializer.data.get("password")

        user = authenticate(username=username, password=password)
        id = user.id
        print(user)
        login(request, user)

        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response({"username": username,'id':user.id, "tokens": tokens}, status=200)



class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # login(request, user)
        return Response(serializer.data, status=201)

class UserPageView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserForUserPageSerializer

    lookup_field = 'id'
from tourapp.models import Tour 
from tourapp.api.serializers import myTourSerializer,TourAddSerializer,TourImageSerializer

class ToursOfUserView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = myTourSerializer
    
    def get_queryset(self):
        queryset = Tour.objects.all()
        id = self.kwargs.get('id')
        return queryset.filter(user = id)
    
from tourapp.models import TourMessages


class MessagesOfTour(generics.ListAPIView):
    queryset = TourMessages
    serializer_class = MessageSerializer
    
    def get_queryset(self):

        queryset = TourMessages.objects.all()
        id = self.kwargs.get('id')
        print(queryset.filter(tour__user = id))
        return queryset.filter(tour__user = id)
    
    
    
from rest_framework.parsers import MultiPartParser

class TourAddView(APIView):
    def post(self, request):
        data = request.data
        serializer = TourAddSerializer(data=data)
        if serializer.is_valid():
            tour = serializer.save()
            image = request.FILES.get('file')
            image_serializer = TourImageSerializer(data={'tour': tour.id, 'image': image})
            if image_serializer.is_valid():
                image_serializer.save()
                return Response({'message': 'success'})
            else:
                #tour.delete() # delete the created tour object if the image serializer is not valid
                return Response(image_serializer.errors)
        else:
            return Response(serializer.errors)
        
    

    
    
