import boto3


# make id-score db
def create_id_score_table(dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	
	table = dynamodb.create_table(
		TableName='id_score',
		KeySchema=[
			{
				'AttributeName': 'id',
				'KeyType': 'HASH'
			},
			{
				'AttributeName': 'score',
				'KeyType': 'RANGE'
			},
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'id',
				'AttributeType': 'S',
			},
			{
				'AttributeName': 'score',
				'AttributeType': 'N',
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 10,
			'WriteCapacityUnits': 10
		}
	)

	return table



if __name__ == '__main__':
	id_score_table = create_id_score_table()
	print("Table status:", id_score_table)
