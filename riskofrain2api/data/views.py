from rest_framework import viewsets

from .serializers.ability import AbilitySerializer
from .serializers.achievement import AchievementSerializer
from .serializers.character import CharacterSerializer
from .serializers.enemy import EnemySerializer
from .serializers.item import ItemSerializer
from .serializers.level import LevelSerializer

from .models.ability import Ability
from .models.achievement import Achievement
from .models.character import Character
from .models.enemy import Enemy
from .models.item import Item
from .models.level import Level


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['get']


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    http_method_names = ['get']


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    http_method_names = ['get']


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
    http_method_names = ['get']


class EnemyViewSet(viewsets.ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer
    http_method_names = ['get']


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    http_method_names = ['get']
