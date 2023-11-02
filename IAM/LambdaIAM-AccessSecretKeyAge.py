import boto3
from datetime import datetime, timezone

def get_accesskey_age(iam,username,key_id):

    # Get the access key
    response = iam.get_access_key_last_used(AccessKeyId=key_id)

    # Extract the LastUsedDate for the access key
    last_used_date =response.get('AccessKeyLastUsed',{}).get('LastUsedDate')

    if last_used_date:
        
        # Convert last_used_date to timezone-aware datetime
        last_used_date = last_used_date.replace(tzinfo=timezone.utc) 
        
        # Calculate the age of the access key
        current_time = datetime.now(timezone.utc) 
        age = current_time - last_used_date
        
        #print the result
        print(f"Last Used Date: {last_used_date}")
        print(f"Age is:{age}")

    else:
        return "Access key has not been used"

def lambda_handler(event, context):

    iam = boto3.client('iam')
    username = "Steve" #Specify the username here....
    key_id = "AKIASM2YUZ4XV3LHDYRD" #Specify the Key id here....

    get_accesskey_age(iam,username,key_id)
