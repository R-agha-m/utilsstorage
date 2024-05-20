
import boto3

session = boto3.Session(
    aws_access_key_id='GzBEWdkOU1IX3jegKcbL',
    aws_secret_access_key='GoQ2WkGkWS3q88nQL9v6AMokTY1eILkec1xQPmqJ',
)


s3 = session.resource('s3',
                      endpoint_url=f'http://127.0.0.1:9000',
                      )

# bucket = s3.Bucket('dms')

# response = bucket.put(
#     Policy = '<policy string here>'
# )


object_acl = s3.ObjectAcl('dms','city/1134.jpg')
response = object_acl.put(ACL='mt_test.py')


# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "s3:GetBucketLocation",
#                 "s3:GetObject"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::*"
#             ]
#         }
#     ]
# }