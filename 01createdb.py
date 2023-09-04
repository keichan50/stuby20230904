# create Dynamodb table
import boto3

boto3.setup_default_session(profile_name='default')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='masashi',
    KeySchema=[
        {
            'AttributeName': 'date',
            'KeyType': 'HASH'  #Partition key
        },
        # {
        #     'AttributeName': 'highest_temperature',
        #     'KeyType': 'RANGE'  #Sort key
        # }
        ],
    AttributeDefinitions=[
        {
            'AttributeName': 'date',
            'AttributeType': 'S'
        },
        # {
        #     'AttributeName': 'highest_temperature',
        #     'AttributeType': 'S'
        # }
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
        }
    )

table.wait_until_exists()
print(table.item_count)
#table.delete()
#table.wait_until_not_exists()
#print(table.item_count)


