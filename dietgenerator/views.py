from django.shortcuts import render
from collections import OrderedDict
import random

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import GenerateDietSerializer, CategorySerializer, GroupSerializer, FoodSerializer
from .models import Group, Category, Food

# ================
#     Utilities
# ================
def selectCategories(group, excludes, category_amount):
  categories = Category.objects.filter(group__id=group).exclude(id__in=excludes)
  categories = categories.order_by('?')[:category_amount]

  return CategorySerializer(categories, many=True).data

def selectFood(category, food_amount):
  foods = Food.objects.filter(category__id=category)
  foods = foods.order_by('?')[:food_amount]

  return FoodSerializer(foods, many=True).data

def calcPortion(imc, food_dict):
  imc_ratio = round(imc) - 25
  portion_ratio = 1 - (imc_ratio*2/100) if imc_ratio > 0 else 1
  food_dict["portion"] = float(food_dict["portion"]) * portion_ratio
  return food_dict

# ================
#     Templates
# ================
def index(request):
  return render(request, 'index.html', {})


# ================
#     Views
# ================
class GenerateDiet(APIView):
  def post(self, request):
    try:
      serializer = GenerateDietSerializer(request.data)
      data = serializer.data
      imc = float(data["weight"]) / (float(data["height"])/100)**2
      categories_per_group = {}

      for group in Group.objects.all():
        categories_per_group[group.name] = selectCategories(group.id, data["exclude_categories"], 1)
        for category in categories_per_group[group.name]:
          category_id = category["id"]
          foods = selectFood(category_id, 2)
          foods = map(lambda x: calcPortion(imc, x), foods)
          category["foods"] = foods
      
      return Response(categories_per_group)
    except:
      return Response({}, status=status.HTTP_400_BAD_REQUEST)


class GroupList(APIView):
  """
  Get all groups
  """
  def get(self, request):
    groups = GroupSerializer(Group.objects.all(), many=True)
    return Response(groups.data)
  
  """
  Post new group
  """
  def post(self, request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)