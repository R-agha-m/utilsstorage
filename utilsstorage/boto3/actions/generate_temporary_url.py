from boto3 import client as _client


def generate_temporary_url(
        client: _client,
        key: str,
        bucket: str,
        server_address_for_client: str,
        endpoint_url: str,
        expires_in: int = 3600,  # seconds
) -> str:
    temp_url = client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        },
        ExpiresIn=expires_in,
    )

    temp_url = temp_url.replace(
        endpoint_url,
        server_address_for_client
    )

    return temp_url
