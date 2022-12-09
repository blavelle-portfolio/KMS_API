import boto3

def lambda_handler(event, context):
    kms = boto3.client('kms')

    method = event['httpMethod']
    body = event['body']

    if method == 'GET':
        # Handle a GET request
        response = kms.list_keys()
        keys = response['Keys']
        return {
            'statusCode': 200,
            'body': json.dumps(keys)
        }
    elif method == 'POST':
        # Handle a POST request
        description = json.loads(body)['description']
        response = kms.create_key(
            Description=description
        )
        key_id = response['KeyMetadata']['KeyId']
        return {
            'statusCode': 201,
            'body': json.dumps({
                'keyId': key_id
            })
        }
    else:
        # Return an error for unsupported methods
        return {
            'statusCode': 405,
            'body': json.dumps({
                'error': f'Method {method} not allowed'
            })
        }
