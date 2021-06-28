import boto3
import datetime

S3_client = boto3.client('s3')
date = datetime.datetime.now()

current_date = "{}-{}-{}".format(date.month, date.day, date.year)

bucket_name = 'aws-bucket-{}'.format(current_date)  #Bucket name
key_value = 'new.jpg' # Key of object in variable
 
#Deleting a object in given bucket 
response = S3_client.delete_object(
    Bucket=bucket_name,
    Key= key_value,
    # MFA='string',
    # VersionId='string',
    # RequestPayer='requester',
    # BypassGovernanceRetention=True|False,
    # ExpectedBucketOwner='string'
)
