from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics

from . import models, serializers


class ShopAPIView(generics.CreateAPIView, generics.RetrieveDestroyAPIView):

    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    lookup_field = "user_id"

    def create(self, request, *args, **kwargs):
        super(ShopAPIView, self).create(request, *args, **kwargs)
        user_id = kwargs["user_id"]
        shops = models.Shop.objects.filter(user_id=user_id)

        if shops:
            return JsonResponse(data="User already has a shop", status=400, safe=False)
        else:
            shop = models.Shop.objects.create(
                user=User.objects.get(user_id=user_id),
                shop_name=request.POST.get("shop_name", "NAN"),
                shop_address=request.POST.get("shop_address", "NAN"),
            )
            shop.save()
            return JsonResponse(data=dict(shop), status=200)


class FoodAPIView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
    lookup_field = "food_id"


class AllFoodAPIView(generics.ListAPIView):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer


class FoodCommentAPIView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FoodComment.objects.all()
    serializer_class = serializers.FoodCommentSerializer
    lookup_field = "food_id"


class OrderAPIView(generics.CreateAPIView, generics.RetrieveDestroyAPIView):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = "user_id"
