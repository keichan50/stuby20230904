import boto3
from boto3.dynamodb.conditions import Key

while True:
    # console input
    act = input('select/insert/delete/quit :')
    if act == 'quit':
        exit()

    boto3.setup_default_session(profile_name='default')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('masashi')

    # select
    if act == 'select':
        # console input
        date = input('date :')

        # select
        response = table.query(
            KeyConditionExpression=Key('date').eq(date)
            )
        
        print(response['Items'])

    # insert
    if act == 'insert':
        # console input
        date = input('date :')
        highest_temperature = input('highest_temperature :')
        lowest_temperature = input('lowest_temperature :')

        # insert
        table.put_item(
            Item={
                'date': date,
                'highest_temperature': highest_temperature,
                'lowest_temperature': lowest_temperature
                }
            )

    # delete
    if act == 'delete':
        # console input
        date = input('date :')

        # delete
        table.delete_item(
            Key={
                'date': date
                }
            )



