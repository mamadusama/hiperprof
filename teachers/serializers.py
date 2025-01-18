from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(
        required=True, min_length=3, max_length=100, source="first_name"
    )
    apelido = serializers.CharField(
        required=True, min_length=3, max_length=100, source="last_name"
    )
    idade = serializers.IntegerField(
        required=True, min_value=18, max_value=100, source="age"
    )
    descricao = serializers.CharField(
        required=True, min_length=10, max_length=500, source="description"
    )
    password_confirmation = serializers.CharField(write_only=True)
    preco_hora = serializers.DecimalField(
        min_value=10,
        max_value=500,
        max_digits=5,
        decimal_places=2,
        required=True,
        source="hourly_price",
    )

    class Meta:
        model = Teacher
        fields = (
            "id",
            "nome",
            "apelido",
            "email",
            "idade",
            "descricao",
            "preco_hora",
            "created_at",
            "updated_at",
            "password",
            "password_confirmation",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

        # validação de password

    def validate_password_confirmation(self, value):
        if self.initial_data["password"] != value:
            raise serializers.ValidationError("As senhas não conferem")
        return value

    def create(self, validated_data):
        del validated_data["password_confirmation"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        del validated_data["password_confirmation"]
        validated_data["password"] = make_password(validated_data["password"])

        return super().update(instance, validated_data)
