import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=False)
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    address = models.TextField()


class Shop(models.Model):
    shop_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    shop_add = models.TextField()


class Food(models.Model):
    shop_id = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
    food_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    food_name = models.CharField(max_length=255)
    food_desc = models.TextField()
    discount_on_food = models.FloatField(default=0)
    food_count = models.IntegerField(default=0)


class FoodComment(models.Model):
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_of_comment = models.DateTimeField(default=datetime.datetime.now)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    date_of_order = models.DateTimeField(default=datetime.datetime.now)
