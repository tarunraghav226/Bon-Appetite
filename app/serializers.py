from rest_framework import serializers

from . import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = "__all__"


class FoodCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodComment
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
