import detect
import boto3
import subprocess 
import json


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('dl-model-aws-connection-image-bucket')
    response = bucket.objects.all()
    s3_files = response["Contents"]
    image = open(s3_files[0], "rb")
    data  = subprocess.run(["detect.py", "--weights", "yolov5x.pt", "--source", image.read()], capture_output=True)
    return json.dumps(data)
