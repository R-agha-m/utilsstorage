from src.setting import CONFIG
from ..connection import connection

bucket_name = CONFIG.MIN_IO.bucket_name
endpoint_url = CONFIG.MIN_IO.endpoint_url
server_address = CONFIG.MIN_IO.server_address


def generate_url(key: str) -> str:
    temp_url = connection().generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket_name,
            'Key': key
        },
        ExpiresIn=3600,
    )

    temp_url = temp_url.replace(
        endpoint_url,
        server_address
    )

    return temp_url
