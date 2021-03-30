import base64
from datetime import datetime
import os

import boto3


def write_to_bucket(event, context):
    s3 = boto3.resource('s3')


    bucket_name = os.environ['BUCKET_NAME']
    now = datetime.utcnow().isoformat()
    key=f'{now}.json'
    s3.Object(bucket_name=bucket_name, key=key).put(Body=base64.standard_b64encode(os.urandom(10)))

    return {
        "message": "Success!",
        "event": event
    }