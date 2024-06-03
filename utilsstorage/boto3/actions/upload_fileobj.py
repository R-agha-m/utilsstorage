from typing import (
    Optional,
    Dict,
    ByteString,
)
from io import (
    BytesIO,
    BufferedReader,
)
from tempfile import SpooledTemporaryFile

from boto3 import client as _client


def upload_fileobj(
        content: ByteString | BytesIO | BufferedReader | SpooledTemporaryFile,
        client: _client,
        key: str,  # /public/dsfsdfsdfsdf.jpg
        content_type: str = None,  # mime_type: "image/jpeg"
        content_disposition: str = None,  # "Content-Disposition": f"attachment; filename={file_name}"
        metadata: Optional[Dict] = None,  # {"user_id: 1, "name": "ali"}
        bucket: Optional[str] = None
) -> None:
    extra_args = dict()
    if metadata:
        extra_args["Metadata"] = metadata

    if content_type:
        extra_args["ContentType"] = content_type

    if content_disposition:
        extra_args["ContentDisposition"] = content_disposition

    if isinstance(content, ByteString):
        content = BytesIO(content)

    client.upload_fileobj(
        Fileobj=content,
        Bucket=bucket,
        Key=key,
        ExtraArgs=extra_args
    )

    return None
