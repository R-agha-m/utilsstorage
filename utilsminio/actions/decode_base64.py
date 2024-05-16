from base64 import b64decode


def decode_base64(base64_string: str) -> bytes:
    return b64decode(base64_string)
