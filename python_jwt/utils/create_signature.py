import hashlib
import hmac


def get_signature(secret_key: str, total_params: str):

    signature: str = hmac.new(
        secret_key,
        total_params,
        hashlib.sha256,
    ).hexdigest()

    return signature
