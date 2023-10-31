import boto3
from datetime import datetime

def get_accesskey_age(iam,username,key_id):

    response = iam.get_access_key_last_used(AccessKeyId=key_id)

    last_used_date =response.get('AccessKeyLastUsed',{}).get('LastUsedDate')

    print(last_used_date)

def lambda_handler(event, context):

    iam = boto3.client('iam')
    username = "Steve" #Specify the username here....
    key_id = "AKIASM2YUZ4XWPJ3OLD3" #Specify the Key id here....

    get_accesskey_age(iam,username,key_id)
