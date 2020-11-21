import json, os

from dietgenerator.models import *

def run():
  curr_path = os.path.dirname(os.path.realpath(__file__))
  json_data = open(f'{curr_path}/media/initial_data.json')   
  data = json.load(json_data)

  group_instances = []
  categories_instances = []
  food_instances = []
  
  try:  
    for group in data["groups"]:
      group_instance = Group(name=group["name"])
      group_instance.save()
      group_instances.append(group_instance)
    
    for category in data["categories"]:
      category_instance = Category(name=category["name"], group=Group.objects.get(id=category["group"]))
      category_instance.save()
      categories_instances.append(category_instance)
    
    for food in data["foods"]:
      food_instance = Food(name=food["name"], portion=food["portion"], portion_unit=food["portion_unit"])
      food_instance.save()
      food_instances.append(food_instance)
      food_instance.category.set(Category.objects.filter(id__in=food["categories"]))
      food_instance.save()
    
    print("Done!")
  except Exception as e:
    print(e)
    for instance in food_instances:
      instance.delete()
    for instance in categories_instances:
      instance.delete()
    for instance in group_instances:
      instance.delete()
  json_data.close()
