from django.shortcuts import render
from . import models
from django.views.generic import ListView
# Create your views here.

class RelationDBView(ListView):
    model = models.Person
    template_name = 'relation_db.html'
    context_object_name = 'nummer_car'
# def relation_db(request):
#     if request.method == 'GET':
#         nummer_car = models.NumberCar.objects.all()
    
#     return render(
#         request,
#         'relation_db.html',
#         {
#             'nummer_car' : nummer_car
#         }
#     )
