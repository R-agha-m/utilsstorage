from boto3 import client as _client


def delete_object(
        client: _client,
        key: str,
        bucket: str,
) -> None:
    client.delete_object(
        Bucket=bucket,
        Key=key,
    )

    return None
