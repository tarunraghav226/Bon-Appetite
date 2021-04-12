from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from django.views import View

from helpers import user_helper

from .models import UserDetails


def home(request):
    return render(request, "home.html", {})


class Register(View):
    def post(self, request):
        user_details = user_helper.get_register_user_data(request.POST)
        print(user_details)

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
