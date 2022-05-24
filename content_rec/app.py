import json
import boto3
import os
def lambda_handler(event, context):
    personalizeRt = boto3.client('personalize-runtime')
    dynamodb_client = boto3.client('dynamodb', region_name=os.environ['REGION'])
    dynamodb = boto3.resource('dynamodb', region_name=os.environ['REGION'])

    CONTENT_TABLE_NAME = os.environ['CONTENT_TABLE_NAME']
    CAMPAIGN_ARN = os.environ['CAMPAIGN_ARN']

    paramString = event['queryStringParameters']
    userId = paramString['userId']

    response = personalizeRt.get_recommendations(
        campaignArn = CAMPAIGN_ARN,
        userId = userId,
        numResults = 20
    )
    recommendationList = response['itemList']
    
    contentList = []
    for item in recommendationList:
        content = dynamodb_client.get_item(
        TableName=CONTENT_TABLE_NAME,
            Key={
                'id': {'S': item['itemId']}
            }
        )
        contentItem = {
            "id": content['Item']['id']['S'],
            "category": content['Item']['category']['S'],
            "content": content['Item']['content']['S'],
            "subject": content['Item']['subject']['S']
        }
        contentList.append(contentItem)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Top picks for you",
            "contentList": contentList
        }),
    }

