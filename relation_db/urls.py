from django.urls import path
from . import views

urlpatterns = [
    path('all_cars/', views.RelationDBView.as_view())
]