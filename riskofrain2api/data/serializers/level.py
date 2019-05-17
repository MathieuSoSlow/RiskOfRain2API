from rest_framework import serializers
from ..models.level import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('name', 'title', 'description')
