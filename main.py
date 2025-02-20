import jwt
from datetime import datetime, timedelta


def create_jwt_token(data: dict, expiration_time: int | None = None) -> str:
    try:
        to_encode = data.copy()
        if not expiration_time:
            exp_time = datetime.utcnow() + timedelta(seconds=35)
        else:
            exp_time = datetime.utcnow() + timedelta(minutes=expiration_time)
        to_encode.update({'exp': exp_time})
        a:str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        return a
    except Exception as e:
        raise e


def get_user(token: str):
    try:
        user_data = jwt.decode(key='1', algorithms='HS256', jwt=token)
        time_difference = datetime.fromtimestamp(float(user_data.get('exp'))) - datetime.utcnow()
        if time_difference < timedelta(seconds=35):
            return "Fail"
        else:
             return "Success"
    except jwt.ExpiredSignatureError as e:
        return "Expired"
