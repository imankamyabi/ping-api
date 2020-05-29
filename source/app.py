import json
import requests
from ping import ping_handler

def lambda_handler(event, context):

    print(event)

    httpMethod = event['httpMethod']
    path = event['resource']

    if httpMethod == 'GET' and path == '/ping':
        return ping_handler(event, context)