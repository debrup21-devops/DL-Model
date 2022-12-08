import os os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import detect
import boto3
import subprocess 
import json


def lambda_handler(event, context):
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket='dl-model-image')['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]
    print(last_added)
    file_path = "https://dl-model-aws-connection-image-bucket.s3.eu-west-2.amazonaws.com/" + last_added
    data  = subprocess.run(["python3", "detect.py", "--weights", "yolov5x.pt", "--source", file_path], capture_output=True)
    print(data)
    
    return json.dumps({"result": "Working"})
