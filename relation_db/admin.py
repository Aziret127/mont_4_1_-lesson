from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.NumberCar)
admin.site.register(models.DocumentCar)
admin.site.register(models.Review)
