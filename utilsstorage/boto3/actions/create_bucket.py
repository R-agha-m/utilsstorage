from boto3 import client as _client


def create_bucket(
        client: _client,
        bucket_name: str,
) -> None:
    """
    AWS provides naming standards when naming an aws bucket.
    -The bucket name can be between 3 and 63 characters long, and can contain only lower-case characters, numbers,
    periods, and dashes.
    -Each label in the bucket name must start with a lowercase letter or number.
    -The bucket name cannot contain underscores, end with a dash, have consecutive periods, or use dashes adjacent
    to periods.
    -The bucket name cannot be formatted as an IP address (198.51.100.24).
    https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html
    """
    exist_buckets = client.list_buckets()
    exist_buckets = {i['Name'] for i in exist_buckets['Buckets']}
    if bucket_name not in exist_buckets:
        client.create_bucket(Bucket=bucket_name)
    return None
