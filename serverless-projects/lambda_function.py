import json
def lambda_handler(event, context):
    # Safely parse query parameters
    query_params = event.get('queryStringParameters', {})
    transactionId = query_params.get('transactionId', '')
    transactionType = query_params.get('type', '')
    transactionAmt = query_params.get('amount', '')
    # Logging for debugging
    print('transactionId=' + transactionId)
    print('transactionType=' + transactionType)
    print('transactionAmt=' + transactionAmt)
    # Construct response object
    transactionResponse = {
        'transactionID': transactionId,
        'type': transactionType,
        'amount': transactionAmt,
        'message': f"Transaction '{transactionId}' of type '{transactionType}' for amount '{transactionAmt}' received successfully."
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(transactionResponse)
    }
