
import json
import boto3

def load_id_score_table(id_score_list, dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	
	table = dynamodb.Table('id_score')

	for id_score_pair in id_score_list:
		id = id_score_pair['id']
		score = id_score_pair['score']
		print("Adding id-score: ", id, score)
		table.put_item(Item=id_score_pair)


if __name__ == '__main__':
	with open("id_score.json") as json_file:
		id_score_list = json.load(json_file)
	
	load_id_score_table(id_score_list)
