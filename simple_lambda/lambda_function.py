import json

def handler(event, context):
    print('Event:', json.dumps(event, indent=2))
    print('Hello from LocalStack Lambda!')
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from LocalStack Lambda!'
        })
    } 