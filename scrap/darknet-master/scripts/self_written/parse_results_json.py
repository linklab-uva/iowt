# break large result json file into json per image in val.txt

import json

json_file = '../../result.json'
results_file = open(json_file, 'r')

output_file = '../../data/val_labels/'

results = json.loads(results_file.read())

for result in results:
	json_name = result['filename'].split('/')[2].split('.')[0] + '_out.json'
	new_json = open(output_file + json_name, 'w')
	new_json.write(json.dumps(result))
	new_json.close()

results_file.close()
