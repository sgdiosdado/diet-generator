from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'portion', 'portion_unit', 'fats', 'protein', 'sodium', 'carbohidrates', 'cholesterol','calories', 'created_at', 'last_updated_at',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
  list_display = ('id', 'name','created_at', 'last_updated_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'created_at', 'last_updated_at',)

admin.site.register(User, UserAdmin)
