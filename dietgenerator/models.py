from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
  pass


class Group(models.Model):
  def __str__(self):
    return f'<Group "{self.name}">'

  name = name = models.CharField(max_length=100, unique=True, blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
  last_updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)


class Category(models.Model):
  class Meta:
    verbose_name_plural = 'categories'

  def __str__(self):
    return f'<Category "{self.name}">'

  name = models.CharField(max_length=100, unique=True, blank=False, null=False)
  group = models.ForeignKey(Group, related_name='categories', null=True, on_delete=models.SET_NULL)
  created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
  last_updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)


class Food(models.Model):
  def __str__(self):
    return f'<Food "{self.name}">'
  
  name = models.CharField(max_length=100, blank=False, null=False)
  portion = models.DecimalField(max_digits=10, decimal_places=2)
  portion_unit = models.CharField(max_length=10, blank=False, null=False, default='g')
  fats = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  sodium = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  carbohidrates = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  cholesterol = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  calories = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) # in Kcal
  category = models.ManyToManyField(Category, related_name='categories')
  created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
  last_updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)