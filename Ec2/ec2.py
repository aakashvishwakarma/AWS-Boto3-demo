import boto3
ec2=boto3.resource('ec2') 
#ec2 = boto3.client('ec2')

# # create a new EC2 instancess

# instances = ec2.create_instances(
#      ImageId='ami-0aeeebd8d2ab47354',
#      #name ="Aakash",
#      MinCount=1,
#      MaxCount=1,
#      InstanceType='t2.micro',
#      KeyName='KEY_PAIR_NAME'
#  )

