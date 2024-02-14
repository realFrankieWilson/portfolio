"""A customised url routing."""
from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.index, name='blog-index'),
]
