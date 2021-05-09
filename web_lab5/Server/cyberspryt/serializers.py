from rest_framework import serializers
from .models import teams

class SerializerData(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:цаии
        model = teams
        fields = '__all__'