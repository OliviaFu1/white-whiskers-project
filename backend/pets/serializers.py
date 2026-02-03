from rest_framework import serializers
from .models import Pet, PetUser

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"
        read_only_fields = ("id",)

class PetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetUser
        fields = "__all__"
        read_only_fields = ("id",)