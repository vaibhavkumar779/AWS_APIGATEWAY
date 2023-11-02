import json
import jwt  # You may need to install this library

def lambda_handler(event, context):
    # Get the token from the request headers
    token = event['headers']['Authorization']

    # Replace 'YOUR_SECRET_KEY' with your actual secret key
    secret_key = 'YOUR_SECRET_KEY'

    try:
        # Verify and decode the token
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        
        # Check if the token is valid and contains the necessary information
        if 'user_id' in payload:
            return generate_policy('user', 'Allow', event['methodArn'])
        else:
            return generate_policy('user', 'Deny', event['methodArn'])
    except jwt.ExpiredSignatureError:
        return generate_policy('user', 'Deny', event['methodArn'])
    except Exception as e:
        return {
            'statusCode': 401,
            'body': json.dumps('Unauthorized')
        }

def generate_policy(principal_id, effect, resource):
    policy = {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }
            ]
        }
    }
    return policy
