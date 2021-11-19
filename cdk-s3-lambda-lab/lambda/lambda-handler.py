import os
import boto3
         
def main(event, context):
    # Print event to logs
    print(event)
    
    s3 = boto3.client('s3')
    bucket_name = os.environ['bucket_name']
    
    response = s3.put_object(
        Bucket=bucket_name,
        Key='sample-object',
        Body='Sample Text'
    )
     
    return {
        'statusCode': 200,
        'body': response
    }