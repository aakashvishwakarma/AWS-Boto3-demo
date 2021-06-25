import boto3
import datetime
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
#Using datetime import to use date

date = datetime.datetime.now()

# Using current date

current_date = "{}-{}-{}".format(date.month, date.day, date.year)

bucket_name = 'aws-bucket-{}'.format(current_date)  #Bucket name
key_value = 'data/test/Boto3' # Key of object in variable

#List objects in current bucket
response = s3_client.list_objects(
    Bucket=bucket_name,
#     Delimiter='string',
#     EncodingType='url',
#     Marker='string',
#     MaxKeys=123,
#     Prefix='string',
#     RequestPayer='requester',
#     ExpectedBucketOwner='string'
)

#upload an file to bucket
response = s3.meta.client.upload_file(Filename='new.jpg', Bucket=bucket_name , Key=key_value)
print(response)
# s3.Bucket(bucket_name).put_object(Key=key_value, Body='new.jpg')
# print(response)
