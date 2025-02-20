import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

reusable_oauth = OAuth2PasswordBearer(
    tokenUrl='/api/v1/account/authorization/',
    scheme_name='jwt'
)


def gen_jwt_token(data: dict, expiration_time: int | None = None) -> dict:
    try:
        to_encode = data.copy()
        if not expiration_time:
            exp_time = datetime.utcnow() + timedelta(minutes=35)
        else:
            exp_time = datetime.utcnow() + timedelta(minutes=expiration_time)
        to_encode.update({'exp': exp_time})
        access: str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        refresh_time = datetime.utcnow() + timedelta(hours=24)
        to_encode.update({'exp': refresh_time})
        refresh: str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        return {
            'access': access,
            'refresh': refresh
        }
    except Exception as e:
        raise e


def get_user(token: str = Depends(reusable_oauth)):
    try:
        user_data = jwt.decode(key='1', algorithms='HS256', jwt=token)
        time_difference = datetime.fromtimestamp(float(user_data.get('exp'))) - datetime.utcnow()
        user_data.update({
            'exp': None
        })
        return user_data
    except jwt.ExpiredSignatureError as e:
        return "Expired"


def refresh_token(
        token: str
):
    try:
        user_data = jwt.decode(key='1', algorithms='HS256', jwt=token)
        to_encode = user_data.copy()
        exp_time = datetime.utcnow() + timedelta(minutes=35)
        to_encode.update({'exp': exp_time})
        access: str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        refresh_time = datetime.utcnow() + timedelta(hours=24)
        to_encode.update({'exp': refresh_time})
        refresh: str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        return {
            'access': access,
            'refresh': refresh
        }
    except jwt.ExpiredSignatureError as e:
        user_data = jwt.decode(key='1', algorithms='HS256', jwt=token)
        to_encode = user_data.copy()
        exp_time = datetime.utcnow() + timedelta(minutes=35)
        to_encode.update({'exp': exp_time})
        access: str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        refresh_time = datetime.utcnow() + timedelta(hours=24)
        to_encode.update({'exp': refresh_time})
        refresh: str = jwt.encode(payload=to_encode, key="1", algorithm="HS256")
        return {
            'access': access,
            'refresh': refresh
        }