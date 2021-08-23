import boto3

def delete_table(table_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table(table_name)
    table.delete()


if __name__ == '__main__':
	table_name = input()
	delete_table(table_name)

