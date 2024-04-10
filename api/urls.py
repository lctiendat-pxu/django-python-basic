from django.urls import path
from . import views

urlpatterns = [
    path("categories", views.CategoryListCreateView.as_view()),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view()),
    path("products", views.ProductListCreateView.as_view()),
    path("products/<int:pk>/", views.ProductDetailView.as_view()),
    path("products/category/<uuid:category_id>/", views.ProductsByCategory.as_view()),

]