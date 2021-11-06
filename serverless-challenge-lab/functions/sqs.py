import boto3
import os
import json

def send_sqs_message(event, context):
  sqs_client = boto3.client('sqs')
  queue_url = os.environ.get('QUEUE_URL')

  response = sqs_client.send_message(
    QueueUrl=queue_url,
    DelaySeconds=0,
    MessageBody=(
      event['headers']['Authorization']
    )
  )

  return {
    'statusCode': 200,
    'body': json.dumps({'messageId': response['MessageId']})
  } 
