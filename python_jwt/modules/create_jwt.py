import base64
import hashlib
import hmac
import json
import logging
from datetime import datetime, timedelta

from utils.base64_encoder import base64url_encode
from utils.create_signature import get_signature

HEADER: dict = {"alg": "HS256", "typ": "JWT"}


class CreateJWT:
    def __init__(self, expiration: int, data: str, secret_key: str):
        self.expiration: int = expiration
        self.data: any = data
        self.secret_key: str = secret_key

    def create_token(self) -> str:
        try:
            date: datetime = datetime.now() + timedelta(minutes=self.expiration)
            expiry: int = int(date.timestamp())
            payload: dict = {"expired": self.expiration, "data": self.data}

            total_params: str = str(base64url_encode(json.dumps(HEADER))) + "." + str(base64url_encode(json.dumps(payload)))

            signature: str = get_signature(
                secret_key=self.secret_key.encode(),
                total_params=total_params.encode(),
            )

            token: str = total_params + "." + str(base64url_encode(signature))
            logging.info("JWT have been successfully created 🔐")
            logging.debug(f" The create JWT {token} ")

        except Exception as error:
            return False

        return token
