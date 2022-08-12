import json

def lambda_handler(event, context):
    meal = event['body']
    if 'love' in meal:
        return {
            'statusCode': 200,
            'body': json.dumps('Lets make a salad')
        }
    return {
        'statusCode': 200,
        'body': json.dumps('Lets make a bbq')
        }
    
