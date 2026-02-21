from django.urls import path
from .views import HelloworldView, NameView, PhotoView

urlpatterns = [
    path('hello/',HelloworldView.as_vaew(), name='hello_world'),
    path('name/',NameView.as_view(), name='name',),
    path('photo/',PhotoView.as_view(), name='photo',),
]