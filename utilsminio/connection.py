import boto3
from botocore.client import Config
from src.setting import CONFIG

endpoint_url = CONFIG.MIN_IO.endpoint_url
access_key_id = CONFIG.MIN_IO.access_key_id
secret_access_key = CONFIG.MIN_IO.secret_access_key
signature_version = CONFIG.MIN_IO.signature_version
region_name = CONFIG.MIN_IO.region_name


# TODO: boto3 is not async, replace it.


def connection() -> boto3.client:
    return boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        config=Config(
            signature_version=signature_version,
            connect_timeout=5,
            retries={"max_attempts": 0},
        ),
        region_name=region_name,
    )