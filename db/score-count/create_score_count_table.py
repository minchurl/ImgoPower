import boto3


# make id-score db
def create_score_count_table(dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	
	table = dynamodb.create_table(
		TableName='score_count',
		KeySchema=[
			{
				'AttributeName': 'score',
				'KeyType': 'HASH'
			},
			{
				'AttributeName': 'count',
				'KeyType': 'RANGE'
			},
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'score',
				'AttributeType': 'N',
			},
			{
				'AttributeName': 'count',
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
	id_score_table = create_score_count_table()
	print("Table status:", id_score_table)
