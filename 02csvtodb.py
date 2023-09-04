import csv
import boto3

boto3.setup_default_session(profile_name='default')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('masashi')

# read csv file
with open('横浜市.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
    for i in range(len(data)):
        if i < 2:
            continue
        line = "{},{},{}".format(data[i][0], data[i][1], data[i][2])
        print(line)

        # dynamobds table insert
        table.put_item(
            Item={
                'date': data[i][0],
                'highest_temperature': data[i][1],
                'lowest_temperature': data[i][2]
                }
                )
        print(table.item_count)

