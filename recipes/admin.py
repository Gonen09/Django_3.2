from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import RecipeIngredient, Recipe

User = get_user_model()

class RecipeIngredientInline(admin.StackedInline): # or admin.TabularInline (horizontal)
    model = RecipeIngredient
    extra = 0 # delete automatically default items number for add 
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial', 'to_ounces']
    #field = ['name', 'quanity', 'unit', 'directions'] # without field all fields are shown

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name','user']
    readonly_fields = ['timestamp','updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)