import re
import boto3
import datetime

from botocore import args
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
#Using datetime import to use date

date = datetime.datetime.now()

# Using current date

current_date = "{}-{}-{}".format(date.month, date.day, date.year)

bucket_name = 'aws-bucket-{}'.format(current_date)  #Bucket name
key_value = 'data/test/Boto3' # Key of object in variable
new_args ={'ACL':'public-read'}

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

#upload single file to bucket

# response = s3.meta.client.upload_file(Filename='new.jpg', Bucket=bucket_name , Key=key_value) #Simple line code
# print(response)

def upload_files(file_name, bucket, Key=None , args=None):  #Function to upload the files
    if Key is None:
        Key=file_name

    response = s3_client.upload_file(file_name, bucket, Key , ExtraArgs = args) #filename=the name of file in local machine , bucket=bucketname, object_name= Key i.e willappear on s3 bucket, arguments)
    print(response)

upload_files('new.jpg',bucket_name, args= new_args)

#Upload a complete folder at once
import glob                 #The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order
files =glob.glob('Data/*')

for file in files:
    upload_files(file,bucket_name, args=new_args)
    print('Uploaded',file)