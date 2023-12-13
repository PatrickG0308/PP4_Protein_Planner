from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "protein",
        "calories",
        "instructions",
        "ingredients",
        "image",
    )
    list_filter = ("meal_type",)
