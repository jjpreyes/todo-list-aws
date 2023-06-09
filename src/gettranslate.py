import json
import decimalencoder
import todoList

def gettranslate(event, context):
    # create a response
    item = todoList.get_item_translate(event['pathParameters']['id'],event['pathParameters']['language'])

    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response