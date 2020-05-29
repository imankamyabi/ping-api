import json


def ping_handler(event, context):
    
    return {
        "statusCode": 200,
        "body": json.dumps({})
    }
