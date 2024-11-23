# Deploy S3 buckets
import boto3

client = boto3.client('s3', region_name='us-east-1')

client.create_bucket(Bucket='prathapbucket-farmersbranch')

with open('myfile.txt', 'w') as file:
    file.write('This is a text file for upload')

client.upload_file(Filename='myfile.txt',
                   Bucket='prathapbucket-farmersbranch',
                   Key='test-upload-file')