from django.shortcuts import render
from collections import OrderedDict
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RecommendedDietSerializer, GenerateDietSerializer, CategorySerializer
from .models import Group, Category

# ================
#     Utilities
# ================
def selectCategories(group, imc, excludes, food_amount):
  imc_ratio = round(imc) - 25
  portion_ratio = 1 - (imc_ratio*2/100) if imc_ratio > 0 else 1

  categories = Category.objects.filter(group__id=group).exclude(id__in=excludes)
  print(categories)
  categories = categories.order_by('?')[:food_amount]

  return categories


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
      protein = selectCategories(1, 24, data["exclude_categories"], 2)
      return Response(CategorySerializer(diet, many=True).data)
    except:
      return Response({}, status=status.HTTP_400_BAD_REQUEST)

class GroupList(APIView):
  """
  Get all groups
  """
  def get(self, request):
    groups = []
    for group in Group.objects.all():
      groups.append({"id": group.id, "name": group.name, "categories": group.categories.values('id', 'name')})
    
    return Response(groups)