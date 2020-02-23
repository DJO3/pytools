import os
import hashlib
import random

import boto3


aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
bucket_name = "blocklist-test"

s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
bucket = s3.Bucket(bucket_name)

rand = random.randrange
blocked_url = f"google.com/this/is/unsafe/"
blocked_url_hash = hashlib.sha256(blocked_url.encode('utf-8')).hexdigest()

print(blocked_url_hash)

hash_object = s3.Object(bucket_name, blocked_url_hash)
hash_object.put(Body=blocked_url)
s3_object = list(bucket.objects.filter(Prefix=blocked_url_hash))
if len(s3_object) > 0 and s3_object[0].key == blocked_url_hash:
    print(f"URL is blocked, hash {s3_object[0].key} found")
else:
    print("URL is not blocked")