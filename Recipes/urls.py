from django.urls import path, include
from .views import *

urlpatterns = [
    path('Recipe/', RecipeView.as_view({'get':'list', 'post':'create'})),
    path('Recipe/<int:pk>/', RecipeView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('Category/', CategoryView.as_view({'get':'list', 'post':'create'})),
    path('Category/<int:pk>/', CategoryView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('Ingredient/', IngredientView.as_view({'get':'list', 'post':'create'})),
    path('Ingredient/<int:pk>/', IngredientView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('register/',register),
    path('login/', login),
]
