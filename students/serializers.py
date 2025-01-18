from rest_framework import serializers
from django.utils import timezone

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(required=True, min_length=3, max_length=100, source='first_name')
    sobrenome = serializers.CharField(required=True, min_length=3 , max_length=100,      source='last_name')
    idade = serializers.IntegerField(required=True, min_value=13, max_value=90,  source='age')
    data_aula = serializers.DateTimeField(required=True, source='clas_date')
    class Meta:
        model = Student
        fields = (
            'id',
            'nome',
            'sobrenome',
            'email',
            'idade',
            'data_aula',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            
        }
        
    def validate_data_aula(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError('A data da aula deve ser no futuro')
        elif value.weekday() > 4:
            raise serializers.ValidationError('As aulas não podem ser marcadas para sábado ou domingo')
        return value
        