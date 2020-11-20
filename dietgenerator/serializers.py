from rest_framework import serializers

from .models import *

class RecommendedDietSerializer(serializers.Serializer):
  protein_name = serializers.CharField(max_length=100)
  protein_portion = serializers.DecimalField(max_digits=10, decimal_places=2)
  plants_name = serializers.CharField(max_length=100)
  plants_portion = serializers.DecimalField(max_digits=10, decimal_places=2)
  cereals_name = serializers.CharField(max_length=100)
  cereals_portion = serializers.DecimalField(max_digits=10, decimal_places=2)


class GenerateDietSerializer(serializers.Serializer):
  weight = serializers.DecimalField(max_digits=5, decimal_places=2)
  height = serializers.DecimalField(max_digits=5, decimal_places=2)
  exclude_categories = serializers.ListField(
    child = serializers.IntegerField()
  )


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']