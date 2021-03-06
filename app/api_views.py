from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView

from app import authentication
from helpers import jwt_authentication_helper

from . import models, serializers


class ShopAPIView(generics.CreateAPIView, generics.RetrieveDestroyAPIView):

    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    lookup_field = "user_id"
    authentication_classes = (authentication.JWTAuthentication,)

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
    authentication_classes = (authentication.JWTAuthentication,)


class AllFoodAPIView(generics.ListAPIView):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer
    authentication_classes = (authentication.JWTAuthentication,)


class FoodCommentAPIView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FoodComment.objects.all()
    serializer_class = serializers.FoodCommentSerializer
    lookup_field = "food_id"
    authentication_classes = (authentication.JWTAuthentication,)


class OrderAPIView(
    generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView
):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = "user_id"
    authentication_classes = (authentication.JWTAuthentication,)


class GenerateAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(username=email, password=password)
        data = {}
        if user:
            data["status"] = 200
            token = jwt_authentication_helper.get_jwt_auth_token(request, user)
            data["auth-token"] = token
        else:
            data["status"] = 404
            data["message"] = "User Not Found"
        return JsonResponse(status=200, data=data)
