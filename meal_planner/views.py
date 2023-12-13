import datetime
import calendar

from django_reorder.reorder import reorder

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models import Q

from .models import Meal
from recipes.models import Recipe

import random


from datetime import timedelta


class MealPlanner(LoginRequiredMixin, TemplateView):
    """View meal planner"""

    template_name = "meal_planner/meal_planner.html"

    def get_context_data(self, **kwargs):
        today = datetime.date.today()

        # Calculate the start and end dates for the upcoming week
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Generate a list of dates for the upcoming week
        days = [start_of_week + timedelta(days=day) for day in range(7)]

        meals = Meal.objects.filter(
            user=self.request.user, meal_date__in=days
        ).order_by(reorder(meal_type=["breakfast", "lunch", "dinner"]))

        context = {"days": days, "meals": meals}

        return context


class GetMeal(TemplateView):
    """
    Class to handle getting a random meal based on
    search queries or empty input
    """

    template_name = "meal_planner/create_meal.html"

    def get_context_data(self, **kwargs):
        protein = self.request.GET.get("protein")
        query = self.request.GET.get("search")

        if query:
            if not protein:
                protein = 9999

            protein = int(protein)
            # Filter by description, title, ingredients,
            # protein value or instructions
            # AND protein & meal type

            recipes = Recipe.objects.filter(
                Q(description__icontains=query)
                | Q(title__icontains=query)
                | Q(ingredients__icontains=query)
                | Q(instructions__icontains=query)
                & Q(protein__lte=protein)
                & Q(meal_type=kwargs["meal_type"])
            )
        # If only protein sent, search by meal type and protein value
        elif protein:
            recipes = Recipe.objects.filter(
                calories__lte=protein, meal_type=kwargs["meal_type"]
            )
        else:
            # if no recipes in the database set empty list
            if len(Recipe.objects.all()) < 1:
                recipes = []
            else:
                # Get random recipe for meal type
                recipes = Recipe.objects.filter(meal_type=kwargs["meal_type"])
        # If recipes returned, get random recipe and return it
        if len(recipes) > 0:
            recipe = random.choice(recipes)
            context = {
                "meal_date": kwargs["meal_date"],
                "meal_type": kwargs["meal_type"],
                "recipe": recipe,
            }
        # If no recipes in database, return without recipe
        else:
            context = {
                "meal_date": kwargs["meal_date"],
                "meal_type": kwargs["meal_type"],
            }

        return context


class AddMeal(View):
    def post(self, *args, **kwargs):
        pk = kwargs["pk"]
        recipe = Recipe.objects.get(pk=pk)
        meal_date = kwargs["meal_date"]
        meal_type = kwargs["meal_type"]

        meal, created = Meal.objects.update_or_create(
            meal_date=meal_date,
            meal_type=meal_type,
            defaults={
                "user": self.request.user,
                "recipe": recipe,
                "meal_date": meal_date,
            },
        )

        return HttpResponseRedirect(reverse("meal_planner"))
