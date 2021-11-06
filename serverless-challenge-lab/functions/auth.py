import boto3
import os

def generate_policy(effect):
  return {
    'principalId': '*',
    'policyDocument': {
      'Version': '2012-10-17',
      'Statement': [
        {
          'Action': 'execute-api:Invoke',
          'Effect': effect,
          'Resource': 'arn:aws:execute-api:*'
        }
      ]
    }
  }


def auth_function(event, context):
  token = event['authorizationToken']

  dynamodb = boto3.client('dynamodb')
  response = dynamodb.get_item(
    TableName=os.environ.get('TABLE_NAME'),
    Key={
      'id': {'S': str(token)}
    }
  )
   
  if response['Item'] and response['Item']['id']['S'] == token:
    print('allow')
    return generate_policy('allow')
  else:
    print('deny')
    return generate_policy('deny')