from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world_view(request):
   if request.method == "GET":
         return HttpResponse("Hello, World!")
   
def name(request):
   if request.method == "GET":
         return HttpResponse('<strong>Radomir Backend Dev</strong>')
   
def photo(request):
   if request.method == "GET":
         return HttpResponse('<img src="https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fakspic.ru%2Falbum%2Fbest_wallpapers%2Ffor_mobile&ved=0CBYQjRxqFwoTCNCClba3tZIDFQAAAAAdAAAAABAj&opi=89978449')
            