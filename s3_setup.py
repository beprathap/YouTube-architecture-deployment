# Deploy S3 buckets
import boto3
from botocore.exceptions import ClientError

# AWS region
region = "us-east-1" # Region can be updated as needed

# Bucket names
buckets = [
    "youtube-raw-data-bucket",
    "youtube-transformed-data-bucket",
    "youtube-mwaa-dags-bucket"
]

# Initialize S3 client
s3_client = boto3.client("s3", region_name=region)

def create_bucket(bucket_name, region):
    """
    Creates an S3 bucket in the specified region
    :param bucket_name:
    :param region:
    :return:
    """

    try:
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint":region}
            )
        print(f"Bucket {bucket_name} created successfully.")
    except ClientError as e:
        print(f"Error creating bucket {bucket_name}: {e}")

# Create buckets
for bucket in buckets:
    create_bucket(bucket, region)
