import datetime

import jwt

from BonAppetite import settings


def get_username_from_jwt(request, *args, **kwargs):
    auth_token = request.headers.get("X-Auth-Token", None)
    payload = jwt.decode(auth_token, key=settings.JWT_SECRET, algorithms=["HS256"])
    return payload.get("sub", None)


def get_jwt_auth_token(request, user, *args, **kwargs):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
        "iat": datetime.datetime.utcnow(),
        "sub": user.username,
    }
    token = jwt.encode(payload=payload, key=settings.JWT_SECRET, algorithm="HS256")
    return token
