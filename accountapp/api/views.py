from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from accountapp.api.serializers import *
from django.contrib.auth import get_user_model, login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.data.get("username")
        password = serializer.data.get("password")

        user = authenticate(username=username, password=password)
        print(user)
        login(request, user)

        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response({"username": username, "tokens": tokens}, status=201)



class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # login(request, user)
        return Response(serializer.data, status=201)
