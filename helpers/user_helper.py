from typing import Dict


def get_register_user_data(request_form_data: Dict):
    user_details = {
        "first_name": request_form_data["fName"],
        "last_name": request_form_data["lName"],
        "email": request_form_data["email"],
        "address": request_form_data["address"],
        "pass1": request_form_data["pass1"],
        "pass2": request_form_data["pass2"],
        "is_merchant": request_form_data.get("merchant", "off") == "on",
    }
    return user_details
