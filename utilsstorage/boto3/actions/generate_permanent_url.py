def generate_permanent_url(
        key: str,
        bucket_name: str,
        server_address_for_client: str,
) -> str:
    return f"{server_address_for_client}/{bucket_name}/{key}"
