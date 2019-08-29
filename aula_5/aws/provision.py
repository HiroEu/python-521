import boto3

def read_credentials():
	headers, content = None, None #fez isso porque PRECISA declarar as variaveis para inicializar

	with open('credentials.csv', 'r') as f:
		headers, content = f.readlines()#separou as duas linhas, em cabeçalho e conteudo
	dictionary = zip(
		headers.strip().split(','),#split vai quebrar na virgula
		content.strip().split(',')#strip arranca os /n
	)
	return {
		k: v for k, v in dictionary
	}

credentials = read_credentials()
# print(credentials)

opts = {
	'aws_access_key_id': credentials['Access key ID'],
	'aws_secret_access_key': credentials['Secret access key'],
	'region_name': 'us-west-2'
}

ec2 = boto3.Session(**opts).resource('ec2')

ec2.create_instances(
	ImageId='ami-082b5a644766e0e6f',
	MinCount=1,
	MaxCount=1,
	TagSpecifications=[
		{
			'ResourceType': 'vpc',
			'Tags': [
				{
					'Key': 'string',
					'Value': 'string'
				},
			]
		}
	]
	)