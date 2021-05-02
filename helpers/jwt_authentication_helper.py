import datetime

import jwt
from rest_framework import exceptions

from BonAppetite import settings


def get_username_from_jwt(request, *args, **kwargs):
    auth_token = request.headers.get("X-Auth-Token", None)
    if not auth_token:
        raise exceptions.AuthenticationFailed("Authentication required.")
    try:
        payload = jwt.decode(auth_token, key=settings.JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed("Token expired")

    return payload.get("sub", None)


def get_jwt_auth_token(request, user, *args, **kwargs):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
        "iat": datetime.datetime.utcnow(),
        "sub": user.username,
    }
    token = jwt.encode(payload=payload, key=settings.JWT_SECRET, algorithm="HS256")
    return token
