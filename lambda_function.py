import json
from urllib import response
import boto3


def lambda_handler(event, context):
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='lambda_ttp_automation',
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=json.dumps({'comando': 'python3 -u /opt/app/automation/index.py'}).encode('utf-8')
    )
    print(response['Payload'].read().decode('utf-8'))
if __name__ == "__main__":
    lambda_handler(event=any, context=any)