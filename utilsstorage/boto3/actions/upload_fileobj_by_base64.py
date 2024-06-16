from typing import (
    Optional,
    Dict,
)
from mimetypes import guess_extension
from base64 import b64decode

from boto3 import client as _client
from utilscommon.utilscommon.exception import ProjectBaseException

from . import upload_fileobj as _upload_fileobj

BASE64_REGEX = "^data:.+/.+;base64,.+$"


def upload_fileobj_by_base64(
        content: str,  # Data URI base64 starts with data:content/type;base64 - example
        client: _client,
        key: str,  # file address like /public/dsfsdfsdfsdf.jpg
        metadata: Optional[Dict] = None,  # {"user_id: 1, "name": "ali"}
        bucket: Optional[str] = None,
        content_disposition: str = None,
) -> str:
    """
    content: str,
    Data URI base64 starts with data:content/type;base64
    example:
    data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQA ...
    """
    mime_type = content.split(";", 1)[0].replace("data:", "")
    extension = guess_extension(type=mime_type)
    if not extension:
        extension = '.' + mime_type \
            .replace("image/", "") \
            .replace('-', '') \
            .replace('+', '')

    content = content.split(",", 1)[1]

    key = f"{key}{extension}"

    try:
        decoded_content = b64decode(content)
    except Exception as e:
        raise ProjectBaseException(
            status_code=422,
            success=False,
            data=None,
            error=str(e),
            message="فرمت base64 ارسالی اشتباه است.",
        )

    _upload_fileobj(
        content=decoded_content,
        client=client,
        content_type=mime_type,
        content_disposition=content_disposition,
        key=key,  # extension has leading .
        metadata={
            'extension': extension,
            **metadata,
        },
        bucket=bucket,
    )

    return key
