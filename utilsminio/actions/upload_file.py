from typing import Optional, Dict, ByteString
from traceback import print_exc
from io import BytesIO, BufferedReader

from src.setting import CONFIG
from ..connection import connection

bucket_name = CONFIG.MIN_IO.bucket_name


def upload_file(
        content: ByteString | BytesIO | BufferedReader,
        content_type: str,  # mime_type: "image/jpeg"
        Key: str,  # /public/dsfsdfsdfsdf.jpg
        metadata: Optional[Dict] = None,  # {"user_id: 1, "name": "ali"}
) -> None:
    extra_args = {
        "Metadata": metadata or dict(),
        "ContentType": content_type
    }

    if isinstance(content, ByteString):
        content = BytesIO(content)

    connection().upload_fileobj(
        Fileobj=content,
        Bucket=bucket_name,
        Key=Key,
        ExtraArgs=extra_args
    )

    return None
