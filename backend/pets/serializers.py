from rest_framework import serializers
from .models import Pet, PetUser


class PetSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "photo_url",
            "species",
            "breed_text",
            "sex",
            "birthdate",
            "date_of_death",
            "weight_kg",
            "created_at",
            "updated_at",
            "role",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "role"]

    def get_role(self, obj: Pet):
        request = self.context.get("request")
        if not request or not request.user or request.user.is_anonymous:
            return None
        link = PetUser.objects.filter(pet=obj, user=request.user).first()
        return link.role if link else None


class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id", "name", "photo_url", "species", "breed_text", "sex", "birthdate", "weight_kg"
        ]
        read_only_fields = ["id"]