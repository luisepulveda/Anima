from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'nombre', 'direccion', 'telefono']

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'nombre', 'direccion', 'telefono']

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            nombre=validated_data['nombre'],
            direccion=validated_data.get('direccion', ''),
            telefono=validated_data.get('telefono', '')
        )
        return user
