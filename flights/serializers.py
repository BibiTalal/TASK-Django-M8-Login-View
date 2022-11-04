from rest_framework import serializers
from .models import Booking, Flight
from django.contrib.auth import get_user_model
User=get_user_model()

class SigninSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        username=data.get("username")
        password=data.get("password")
        
        try:
         user=User.objects.get(username=username)
         if user.check_password(password):
             return data

        except User.DoesNotExist:
            raise serializers.ValidationError("User Does Not Exist!!")
        else:
            raise serializers.ValidationError("Incorrect Password")

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","password","first_name","last_name"]
    
    def create(self, validated_data):
        username=validated_data["username"]
        password=validated_data["password"]
        new_user=User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["destination", "time", "price", "id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "passengers", "id"]


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["date", "passengers"]
