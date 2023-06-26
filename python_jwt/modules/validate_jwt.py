import base64
import hashlib
import hmac
import logging
import re

from utils.base64_encoder import base64url_encode
from utils.create_signature import get_signature


class ValidateJWT:
    def __init__(self, token: str, secret_key: str):
        self.token: str = token
        self.secret_key: str = secret_key

    def validate_token(self) -> bool:

        try:
            token_sections = re.split(r"[-;,.\s]\s*", self.token)
            total_params: str = token_sections[0] + "." + token_sections[1]

            signature: str = get_signature(
                secret_key=self.secret_key.encode(),
                total_params=total_params.encode(),
            )

            token_verify: str = total_params + "." + str(base64url_encode(signature))

            if token_verify != self.token:
                logging.error("Invalid token")

            if token_verify == self.token:
                logging.info("Valid token")

        except Exception as error:
            return False

        return True
