from typing import (
    Optional,
    Dict,
)
from mimetypes import guess_extension
from base64 import b64decode

from boto3 import client as _client



def make_dir_public(
        client: _client,
        bucket: Optional[str] = None,
        prefix: Optional[str] = None,
):
    # bucket = s3.Bucket(bucket_name)
    # bucket = client.Bucket(bucket)

    # result = client.get_bucket_acl(Bucket=bucket)
    # print(result)

    response = client.put_bucket_acl(
        ACL='public-read',
        # AccessControlPolicy={
        #     'Grants': [
        #         {
        #             'Grantee': {
        #                 'DisplayName': 'string',
        #                 'EmailAddress': 'string',
        #                 'ID': 'string',
        #                 'Type': 'CanonicalUser' | 'AmazonCustomerByEmail' | 'Group',
        #                 'URI': 'string'
        #             },
        #             'Permission': 'FULL_CONTROL' | 'WRITE' | 'WRITE_ACP' | 'READ' | 'READ_ACP'
        #         },
        #     ],
        #     'Owner': {
        #         'DisplayName': 'string',
        #         'ID': 'string'
        #     }
        # },
        Bucket=bucket,
        # ChecksumAlgorithm='CRC32' | 'CRC32C' | 'SHA1' | 'SHA256',
        # GrantFullControl='string',
        # GrantRead='string',
        # GrantReadACP='string',
        # GrantWrite='string',
        # GrantWriteACP='string',
        # ExpectedBucketOwner='string'
    )

    # response = client.put_object_acl(
    #     ACL='public-read',
    #     Bucket=bucket,
    #     # ChecksumAlgorithm='CRC32' | 'CRC32C' | 'SHA1' | 'SHA256',
    #     # GrantFullControl='string',
    #     # GrantRead='string',
    #     # GrantReadACP='string',
    #     # GrantWrite='string',
    #     # GrantWriteACP='string',
    #     Key='city/1134.jpg',
    #     # RequestPayer='requester',
    #     # VersionId='string',
    #     # ExpectedBucketOwner='string'
    # )

    # response = bucket.put(
    #     Policy='<policy string here>'
    # )
    return None

# response = client.put_object_acl(
#     ACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exec-read'|'bucket-owner-read'|'bucket-owner-full-control',
#     AccessControlPolicy={
#         'Grants': [
#             {
#                 'Grantee': {
#                     'DisplayName': 'string',
#                     'EmailAddress': 'string',
#                     'ID': 'string',
#                     'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
#                     'URI': 'string'
#                 },
#                 'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
#             },
#         ],
#         'Owner': {
#             'DisplayName': 'string',
#             'ID': 'string'
#         }
#     },
#     Bucket='string',
#     ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
#     GrantFullControl='string',
#     GrantRead='string',
#     GrantReadACP='string',
#     GrantWrite='string',
#     GrantWriteACP='string',
#     Key='string',
#     RequestPayer='requester',
#     VersionId='string',
#     ExpectedBucketOwner='string'
# )