import json
temp_file = open('./ibm_credentials.json', 'r')

temp_file = temp_file.read()

json = json.loads(temp_file)

print(type(json), json['ibm_username'])
