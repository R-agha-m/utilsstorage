from base64 import b64decode

from src.storage.min_io.function.upload_file import upload_file
from src.storage.min_io.function.generate_random_string import generate_random_string


def convert_base64_image_to_key(content: str) -> str:
    mime_type = content.split(";")[0].replace("data:", "")
    extension = mime_type.replace("image/", "")
    content = ",".join(content.split(",")[1:])
    content = b64decode(content)

    random_str = generate_random_string(length=20)

    object_name = f"public/{random_str}.{extension}"
    upload_file(
        content=content,
        content_type=mime_type,
        Key=object_name,
        metadata=None,
    )

    return object_name
