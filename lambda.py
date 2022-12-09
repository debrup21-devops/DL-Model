import os 
os.environ['MPLCONFIGDIR'] = os.getcwd()
import detect
import boto3
import subprocess 
import json
import numpy as np
import cv2
    

def save_file(context, i):
    string = context
    encoded_string = string
    bucket_name = "dl-model-aws-connection-image-bucket"
    file_name = "hello"+i+".txt"
    s3_path = "outputs/" + file_name
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)


def lambda_handler(event, context):
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket='dl-model-image')['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]
    print(last_added)
    file_path = "https://dl-model-aws-connection-image-bucket.s3.eu-west-2.amazonaws.com/" + last_added
    image_obj = s3.get_object(Bucket='dl-model-image', Key=last_added)
    image_data = image_obj["Body"].read()
    np_array = np.frombufffer(image_data, np.uint8)
    
    data  = subprocess.run(["python3", "detect.py", "--weights", "yolov5x.pt", "--source", np_array,  "--save-txt"], universal_newlines = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
    save_file(data.stdout, "a")
    save_file(data.stderr, "c")
    data = subprocess.run(["ls", "-l"], universal_newlines = True, stdout = subprocess.PIPE)
    save_file(data.stdout, "b")
    
    return json.dumps({"result": "Working"})
