import boto3
import datetime

# adding resources and clients as per the interface
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')

#Using datetime import to use date

date = datetime.datetime.now()

current_date = "{}-{}-{}".format(date.month, date.day, date.year)

bucket_name = 'aws-bucket-{}'.format(current_date)  #Bucket name
key_value = 'data/test/Boto3' # Key of object in variable

# Code to print all the bucket present in AWS account
for bucket in s3.buckets.all():
    print(bucket.name)

# Code to create a bucket
bucket =s3.Bucket(bucket_name) 
if bucket in s3.buckets.all() :   #loop to check if bucket exist don't create else create bucket
    print("bucket exist")
else:
    response = s3_client.create_bucket(
    ACL='private',
    Bucket=bucket_name,
        # CreateBucketConfiguration={
        #      'LocationConstraint': 'us-west-1'},
    # GrantFullControl='string',
    # GrantRead='string',
    # GrantReadACP='string',
    # GrantWrite='string',
    # GrantWriteACP='string',
    # ObjectLockEnabledForBucket=True|False
)
print(response)