from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import MenuItemForm, IngredientForm, PurchaseForm

def home(request):
  return render(request, "inventory/index.html")

# below: views that let the user see current inventory,
# add new ingredients, update stock and delete ingredients

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class MenuListView(LoginRequiredMixin, ListView):
     model = MenuItem
     template_name = "inventory/menu.html"


# view that decreases ingredient quantities in stock and registers purchases made

class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/add_purchase.html"
