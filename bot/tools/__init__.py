import boto3
import json
from settings import AWS_S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class S3Helper:

    def __init__(self):
        self.s3 = boto3.resource('s3',
                                 aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    def get_words(self):
        beer_styles_obj = self.s3.Object(AWS_S3_BUCKET_NAME, f"words_500.json")
        body = beer_styles_obj.get()['Body'].read().decode("utf-8")
        return json.loads(body)

