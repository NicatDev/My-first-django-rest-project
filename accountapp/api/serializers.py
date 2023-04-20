from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.conf import settings


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", 'first_name','email')
        
class UserForUserPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name','id', 'first_name','email')
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})


    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({"Sifre ve ya email yalnisdir"})
        return attrs



class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username',"email", "password","first_name")
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        email_qs = User.objects.filter(email=email).exists()

        if email_qs:
            raise serializers.ValidationError({"Bu email ile artiq qeydiyyatdan kecilib"})

        if len(password) < 6:
            raise serializers.ValidationError({"Sifre en azi 6 simvoldan ibaret olmalidir"})

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(
            **validated_data
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save()

        # send mail
        send_mail(
            'Qeydiyyat tamamla',
            f'Hormetli {user.first_name}!  Siz camp saytimizdan qeydiyyatdan kecmisiz, Son teklif ve kampaniyalar email unvaniniza gonderilecek',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return user


from tourapp.models import TourMessages

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourMessages
        fields = '__all__'

class ContactUsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=120)
    
    def create(self,instance):
        name = instance.get('name')
        message = instance.get('message')
        email = instance.get('email')
       
        send_mail(
            'Size Azkampdan bildiris var !',
            f'Hormetli {name} bey/xanim! Sizin mektubunuz ugurla qebul edildi ve tezlikle cavablandirilacaqdir !',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return {'as':'as'}
        