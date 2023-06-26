import base64


def base64url_encode(input: str) -> str:
    byte_string = input.encode("ascii")
    string_base = base64.urlsafe_b64encode(byte_string).decode("utf-8").replace("=", "")
    return string_base
