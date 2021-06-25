import boto3
import datetime

S3_client = boto3.client('s3')
date = datetime.datetime.now()

current_date = "{}-{}-{}".format(date.month, date.day, date.year)
bucket_name = 'aws-bucket-{}'.format(current_date)  # Bucket name

#Deleting a object in given bucket 
response = S3_client.delete_bucket(
    Bucket= bucket_name,
    #ExpectedBucketOwner='string',  # The account ID of the expected bucket owner. If the bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    # MFA='string',
    # VersionId='string',
    # RequestPayer='requester',
    # BypassGovernanceRetention=True|False,
    # ExpectedBucketOwner='string'
)