import boto3
ec2 = boto3.resource('ec2')
# Create a file to store the key locally

# outfile = open('ec2-keypair.pem','w')

# call the boto ec2 function to create a key pair

# key_pair = ec2.create_key_pair(KeyName='KEY_PAIR_NAME')

# capture the key and store it in a file

# KeyPairOut = str(key_pair.key_material)
# print(KeyPairOut)
# outfile.write(KeyPairOut)

# 2nd method to create a file to store the key locally

response = ec2.create_key_pair(KeyName='KEY_PAIR_NAME')
print(response)


