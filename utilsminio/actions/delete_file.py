from src.setting import CONFIG
from ..connection import connection

bucket_name = CONFIG.MIN_IO.bucket_name


def delete_file(key: str) -> None:
    connection().delete_object(
        Bucket=bucket_name,
        Key=key,
    )

    return None
