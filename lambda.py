import detect
import boto3
import subprocess 
import json


def lambda_handler(event, context):
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('dl-model-aws-connection-image-bucket')
#     response = bucket.objects.all()
#     s3_files = response["Contents"]
#     image = open(s3_files[0], "rb")
    file_path = "https://dl-model-aws-connection-image-bucket.s3.eu-west-2.amazonaws.com/track.jpeg"
    data  = subprocess.run(["python3", "detect.py", "--weights", "yolov5x.pt", "--source", file_path], capture_output=True)
    print(data)
    
    return json.dumps({"result": data})
