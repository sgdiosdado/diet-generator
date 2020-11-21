from rest_framework import serializers

from .models import *


class GenerateDietSerializer(serializers.Serializer):
  weight = serializers.DecimalField(max_digits=5, decimal_places=2)
  height = serializers.DecimalField(max_digits=5, decimal_places=2)
  exclude_categories = serializers.ListField(
    child = serializers.IntegerField()
  )


class FoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Food
    fields = ['id', 'name', 'portion', 'portion_unit']


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']
  

class GroupSerializer(serializers.ModelSerializer):
  categories = CategorySerializer(many=True, required=False, read_only=True)

  class Meta:
    model = Group
    fields = ['id', 'name', 'categories']

