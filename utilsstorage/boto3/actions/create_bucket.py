from boto3 import client as _client


def create_bucket(
        client: _client,
        bucket_name: str,
):
    exist_buckets = client.list_buckets()
    exist_buckets = {i['Name'] for i in exist_buckets['Buckets']}
    if bucket_name not in exist_buckets:
        client.create_bucket(Bucket=bucket_name)
    return
