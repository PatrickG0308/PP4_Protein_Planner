from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class AddRecipe(LoginRequiredMixin, CreateView):    

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
