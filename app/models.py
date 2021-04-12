import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=False)
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    address = models.TextField()


class Shop(models.Model):
    shop_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=40, default=None)
    shop_address = models.TextField()


def get_image_address(instance, filename):
    return "user_{0}/{1}".format(instance.shop_id.user.username, filename)


class Food(models.Model):
    shop_id = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
    food_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    food_name = models.CharField(max_length=255)
    food_desc = models.TextField()
    discount_on_food = models.FloatField(default=0)
    food_count = models.IntegerField(default=0)
    food_image = models.ImageField(upload_to=get_image_address, default=None)
    food_price = models.FloatField(default=0)


class FoodComment(models.Model):
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_of_comment = models.DateTimeField(default=datetime.datetime.now)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    date_of_order = models.DateTimeField(default=datetime.datetime.now)
