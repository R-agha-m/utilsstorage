from typing import (
    Optional,
    Dict,
    ByteString,
)
from io import (
    BytesIO,
    BufferedReader,
)

from boto3 import client as _client


def upload_fileobj(
        content: ByteString | BytesIO | BufferedReader,
        client: _client,
        content_type: str,  # mime_type: "image/jpeg"
        key: str,  # /public/dsfsdfsdfsdf.jpg
        metadata: Optional[Dict] = None,  # {"user_id: 1, "name": "ali"}
        bucket: Optional[str] = None
) -> None:
    extra_args = dict()
    if metadata:
        extra_args["Metadata"] = metadata

    if content_type:
        extra_args["ContentType"] = content_type

    if isinstance(content, ByteString):
        content = BytesIO(content)

    result = client.upload_fileobj(
        Fileobj=content,
        Bucket=bucket,
        Key=key,
        ExtraArgs=extra_args
    )

    return None
