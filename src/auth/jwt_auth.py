import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

from config import AUTH_KEY, AUTH_ALGORITHM, AUTH_ACCESS_TOKEN_EXPIRE_TIME


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_auth_key = AUTH_KEY
    expired_time = AUTH_ACCESS_TOKEN_EXPIRE_TIME
    algorithm = AUTH_ALGORITHM

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=int(self.expired_time)),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret_auth_key
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_auth_key, algorithms=[self.algorithm])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=403, detail='Token has been expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=403, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)
