from typing import Optional

from boto3 import client as _client


def list_objects(
        client: _client,
        bucket: Optional[str] = None,
        prefix: Optional[str] = None,
):
    return client.list_objects(
        Bucket=bucket,
        Prefix=prefix,
    )
