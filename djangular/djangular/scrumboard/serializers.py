from rest_framework import serializers
from .models import List, Card


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'  # all model fields will be included


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'  # all model fields will be included
