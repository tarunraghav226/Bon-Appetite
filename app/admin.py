from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserDetails)
admin.site.register(models.Shop)
admin.site.register(models.Food)
admin.site.register(models.FoodComment)
admin.site.register(models.Order)
