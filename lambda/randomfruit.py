import json


def lambda_handler(event, context):
    fruit = event["fruit"]
    print(f'THIS IS THE {event}')
    if fruit == 'cherry':
        return {
            'statusCode': 200,
            'body': json.dumps(f'I love {fruit}')
        }
    return {
            'statusCode': 200,
            'body': json.dumps(f"No thanks I don't like {fruit}" )
        }