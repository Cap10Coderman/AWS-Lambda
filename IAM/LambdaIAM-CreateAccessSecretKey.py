import boto3

def create_keys(username):
    
    # Initialize the IAM client
    iam = boto3.client('iam')
    
    # Create access keys for the user
    access_key_response = iam.create_access_key(UserName=username)
    
    # Return the access key and secret key
    access_key = access_key_response['AccessKey']
    return {
        'AccessKeyId': access_key['AccessKeyId'],
        'SecretAccessKey': access_key['SecretAccessKey']
    }
    
def lambda_handler(event, context):
    
    # Specify the username for the IAM user
    username = 'Steve' 
    
    # Function call to create the user and keys
    result = create_keys(username)
    
    # Print the access key and secret key
    print(f"Access Key ID: {result['AccessKeyId']}")
    print(f"Secret Access Key: {result['SecretAccessKey']}")
    
    # You can return the keys as a response, if needed
    return result