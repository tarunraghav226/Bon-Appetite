def get_food_details(request):
    food_details = {
        "food_name": request.POST["food_name"],
        "food_desc": request.POST["food_desc"],
        "discount_on_food": request.POST["discount_on_food"],
        "food_count": request.POST["food_count"],
        "food_price": request.POST["food_price"],
        "food_image": request.FILES["food_image"],
    }

    return food_details
