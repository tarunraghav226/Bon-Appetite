from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View

from helpers import food_helper, user_helper

from .models import Food, Order, Shop, UserDetails


def home(request):
    context = {}
    if request.user.is_authenticated:
        user = UserDetails.objects.filter(user=request.user)[0]
        context["is_seller"] = user.is_seller
    return render(request, "home.html", context)


class Register(View):
    def post(self, request):
        user_details = user_helper.get_register_user_data(request.POST)

        if user_details["pass1"] == "":
            messages.error(request, "Password cannot be empty")
            return redirect("/")

        if user_details["pass1"] != user_details["pass2"]:
            messages.error(request, "Password and confirm password not matched")
            return redirect("/")

        if User.objects.filter(email=user_details["email"]):
            messages.error(request, "Email already registered")
            return redirect("/")

        user = User.objects.create_user(
            first_name=user_details["first_name"],
            last_name=user_details["last_name"],
            username=user_details["email"],
            email=user_details["email"],
            password=user_details["pass1"],
        )
        user_other_details = UserDetails.objects.create(
            user=user,
            address=user_details["address"],
            is_seller=user_details["is_merchant"],
        )
        user.save()
        user_other_details.save()

        messages.info(request, "Successfully registered.")
        return redirect("/")


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "User not found")
            return redirect("/")


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect("/")


class ShopView(View):
    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller

        shop = Shop.objects.filter(user=request.user)
        if shop:
            context["shop"] = shop[0]
            foods = Food.objects.filter(shop_id=shop[0].shop_id)
            if foods:
                context["foods"] = foods
            return render(request, "shop.html", context)
        else:
            return render(request, "shop.html", context)

    def post(self, request):
        shop = Shop.objects.filter(user=request.user)

        if shop:
            messages.error(request, "You already have one shop")
            return redirect("/shop/")

        shop = Shop.objects.create(
            user=request.user,
            shop_name=request.POST["shop_name"],
            shop_address=request.POST["shop_address"],
        )
        shop.save()
        return redirect("/shop/")


class FoodView(View):
    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller

        return render(request, "add-food.html", context)

    def post(self, request):
        food_details = food_helper.get_food_details(request)
        shop = Shop.objects.filter(user=request.user)

        if float(food_details["discount_on_food"]) < 0:
            messages.error(request, "Discount must be positive")
            return redirect("/add-food/")

        if float(food_details["food_count"]) < 0:
            messages.error(request, "Food count must be positive")
            return redirect("/add-food/")

        if float(food_details["food_price"]) < 0:
            messages.error(request, "Food price must be positive")
            return redirect("/add-food/")

        if not shop:
            messages.error(request, "No shop found")
            return redirect("/")

        new_food = Food.objects.create(
            shop_id=shop[0],
            food_name=food_details["food_name"],
            food_desc=food_details["food_name"],
            discount_on_food=food_details["discount_on_food"],
            food_count=food_details["food_count"],
            food_image=food_details["food_image"],
            food_price=food_details["food_price"],
        )

        new_food.save()
        return redirect("/shop/")


class EditFoodView(View):
    def get(self, request, id):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller

        shop = Shop.objects.filter(user=request.user)

        if not shop:
            messages.error(request, "You are not allowed to perform this action.")
            return redirect("/shop/")

        food = Food.objects.filter(food_id=id)

        if not food:
            messages.error(request, "Food not found.")
            return redirect("/shop/")

        if food[0].shop_id.shop_id != shop[0].shop_id:
            messages.error(request, "You are not allowed to perform this action.")
            return redirect("/shop/")

        context["food"] = food[0]
        context["edit"] = True
        return render(request, "add-food.html", context)

    def post(self, request):
        food_details = food_helper.get_food_details(request)
        shop = Shop.objects.filter(user=request.user)

        if float(food_details["discount_on_food"]) < 0:
            messages.error(request, "Discount must be positive")
            return redirect("/add-food/")

        if float(food_details["food_count"]) < 0:
            messages.error(request, "Food count must be positive")
            return redirect("/add-food/")

        if float(food_details["food_price"]) < 0:
            messages.error(request, "Food price must be positive")
            return redirect("/add-food/")

        if not shop:
            messages.error(request, "No shop found")
            return redirect("/")

        food = Food.objects.filter(shop_id=shop[0], food_id=request.POST["food_id"])

        if not food:
            print(food)
            messages.error(request, "Updation failed")
            return redirect("/")

        food = food[0]
        food.food_name = food_details["food_name"]
        food.food_desc = food_details["food_desc"]
        food.discount_on_food = food_details["discount_on_food"]
        food.food_count = food_details["food_count"]
        food.food_price = food_details["food_price"]

        if food_details["food_image"]:
            food.food_image = food_details["food_image"]

        food.save()
        return redirect("/shop/")


class DeleteFoodView(View):
    def get(self, request, id):
        shop = Shop.objects.filter(user=request.user)

        if not shop:
            messages.error(request, "Failed to delte")
            return redirect("/shop/")
        shop = shop[0]

        food = Food.objects.filter(food_id=id, shop_id=shop)

        if not food:
            messages.error(request, "You are not allowed to perform this action.")
            return redirect("/shop/")
        food = food[0]
        food.delete()
        return redirect("/shop/")


class ShowFoodView(View):
    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller
        foods = Food.objects.all()
        context["foods"] = foods
        return render(request, "show-food.html", context)


class ShowView(View):
    def get(self, request, id):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller

        food = Food.objects.filter(food_id=id)
        if not food:
            messages.error(request, "No food found.")
            return "/show-food/"
        food = food[0]
        context["food"] = food
        return render(request, "show.html", context)


class SearchView(View):
    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller

        search_vals = request.GET.get("search", "").split(" ")

        if not search_vals:
            return redirect("/show-food/")

        foods = []

        for search_val in search_vals:
            foods.append(
                Food.objects.filter(
                    Q(food_name__contains=search_val)
                    | Q(food_desc__contains=search_val)
                )
            )
        foods = list(food[0] for food in foods if food)
        context["foods"] = foods
        if not foods:
            messages.error(request, "No food found.")
        return render(request, "show-food.html", context)


class BuyView(View):
    def get(self, request, id):
        context = {}

        if request.user.is_authenticated:
            user = UserDetails.objects.filter(user=request.user)[0]
            context["is_seller"] = user.is_seller

        food_obj = Food.objects.filter(food_id=id, food_count__gt=0)

        if not food_obj:
            messages.error(request, "No food detail found")
            return redirect("/shop/")
        food_obj = food_obj[0]

        context["food"] = food_obj
        context["price_after_discount"] = food_obj.food_price - (
            (food_obj.food_price * food_obj.discount_on_food) / 100
        )

        return render(request, "checkout.html", context=context)


class OrderView(View):
    def get(self, request, id):
        food = Food.objects.filter(food_id=id)
        if not food:
            messages.error(request, "No food found")
            return redirect("/shop/")
        food = food[0]
        order = Order.objects.create(user=request.user, food=food)
        order.save()
        food.food_count -= 1
        food.save()
        return redirect("/orders/")
