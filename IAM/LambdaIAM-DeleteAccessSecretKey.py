import boto3

#Deactivating the Access Key   
def deactivate_key(iam, user_name,  key_id):
    iam.update_access_key(UserName=user_name, AccessKeyId=key_id, Status='Inactive')
    print(f"Deactivated access key {key_id} for user {user_name}")

#Deleting the Access Key
def delete_key(iam, user_name, key_id):
    iam.delete_access_key(UserName=user_name, AccessKeyId=key_id)
    print(f"Deleted access key {key_id} for user {user_name}")
    
def lambda_handler(event, context):
    
    #Initialize the IAM client
    iam = boto3.client('iam')

    # Specify the username for the IAM user 
    username = 'Steve' 

    # Specify the Access keyID for the IAM user 
    key_id = 'AKIASM2YUZ4X3CRTSM6K' 
    
    # Function call to deactivate the user and keys
    deactivate_key(iam,username,key_id)

    # Function call to delete the user and keys
    delete_key(iam,username,key_id)
    
    # You can return the keys as a response, if needed
    # return result