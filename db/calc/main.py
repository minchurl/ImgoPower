
import boto3


def scan_id_score_table(dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	
	table = dynamodb.Table('id_score')

	response = table.scan()
	res = response.get('Items', [])

	return res

def calc(id_score_list):
	cnt = [0 for _ in range(0, 101)]
	for pair in id_score_list:
		score = int(pair['score'])
		cnt[score] = cnt[score] + 1
	
	score_count_list = []

	min = 0
	for i in range(0, 101):
		if (cnt[i]):
			min = i
			break
	
	max = 100 
	for i in range(100, -1, -1):
		if (cnt[i]):
			max = i
			break
	

	for i in range(min, max + 1):
		score_count_list.append({
			'score': i,
			'count': cnt[i]
		})
	
	return score_count_list

	
def load_score_count_table(score_count_list, dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
	
	table = dynamodb.Table('score_count')

	for score_count_pair in score_count_list:
		score = score_count_pair['score']
		count = score_count_pair['count']
		print("Adding id-score: ", score, count)
		table.put_item(Item=score_count_pair)


if __name__ == '__main__':
	id_score_list = scan_id_score_table()
	score_count_list = calc(id_score_list)
	load_score_count_table(score_count_list)
	