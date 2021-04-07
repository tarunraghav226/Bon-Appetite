from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from django.views import View


def home(request):
    return render(request, "home.html", {})


class Register(View):
    def get(self, request):
        return render(request, "register.html", {})

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password1,
        )
        user.save()
        print("user created")
        return redirect("/")
