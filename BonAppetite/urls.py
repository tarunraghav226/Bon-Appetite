"""BonAppetite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views
from . import settings

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("shop/", views.ShopView.as_view(), name="shop"),
    path("edit/", views.EditFoodView.as_view(), name="edit"),
    path("edit/<str:id>/", views.EditFoodView.as_view(), name="edit"),
    path("delete/<str:id>/", views.DeleteFoodView.as_view(), name="delete"),
    path("add-food/", views.FoodView.as_view(), name="add_food"),
    path("show-food/", views.ShowFoodView.as_view(), name="show_food"),
    path("show/<str:id>", views.ShowView.as_view(), name="show"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("buy/<str:id>", views.BuyView.as_view(), name="buy"),
    path("order/<str:id>", views.OrderView.as_view(), name="order"),
    path("orders/", views.ShowOrderView.as_view(), name="orders"),
    path("comment/", views.CommentView.as_view(), name="comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
