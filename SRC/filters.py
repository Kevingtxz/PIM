import django_filters
from .models import *

class MentorFilter(django_filters.FilterSet):
    class Meta:
        model = Mentor
        fields = ['education_Level', 'nickname', 'elo', 'region',]

class MissionFilter(django_filters.FilterSet):
    class Meta:
        model = Mission
        fields = ['region', 'text', 'title', 'elo',]