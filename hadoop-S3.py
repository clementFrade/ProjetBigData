import os
import boto3

os.system('hadoop fs -copyToLocal -f /user/maria_dev/projetBigData/* /home/maria_dev')
s3_client = boto3.client('s3')
response=s3_client.upload_file('/home/maria_dev/predict.csv','pbd-cty','predict.csv')
response=s3_client.upload_file('/home/maria_dev/train.csv','pbd-cty','train.csv')