import uuid
import json
import boto3

def generate_token(event, context):
  token = "ca-lab." + str(uuid.uuid4())

  dynamodb = boto3.client('dynamodb')

  dynamodb.put_item(
    TableName='tokensTable',
    Item={
      'id': {'S': token}
    }
  )

  return {
    'statusCode': 201,
    'body': json.dumps({'token': token})
  }