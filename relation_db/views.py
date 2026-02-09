from django.shortcuts import render
from . import models
# Create your views here.


def relation_db(request):
    if request.method == 'GET':
        nummer_car = models.NumberCar.objects.all()
    
    return render(
        request,
        'relation_db.html',
        {
            'nummer_car' : nummer_car
        }
    )
