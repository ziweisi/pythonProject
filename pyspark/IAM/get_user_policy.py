


import boto3

client = boto3.client('iam')

# response = client.get_user_policy(
#     UserName='sziwei',
#     PolicyName='AdminUser'
# )


response = client.list_user_policies(
    UserName='sziwei',
    MaxItems=100
)
print(response)