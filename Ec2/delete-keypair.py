import boto3
ec2 =boto3.client('ec2')

# #To delete the keypair
response = ec2.delete_key_pair(KeyName='KEY_PAIR_NAME')
print(response)

# ec2 =boto3.resource('ec2')
# key_pair = ec2.KeyPair('KEY_PAIR_NAME')

# response = key_pair.delete(
#     KeyPairId='key-0ddeb219a2326a5cb',
# )