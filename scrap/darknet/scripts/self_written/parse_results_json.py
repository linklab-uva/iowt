'''
Break large result json file into json per image in json, saves smaller jsons to data/val_labels.

result.json must be created with ./darknet detector test data/obj.data data/obj.cfg backup/obj_best.weights -ext_output -dont_show -out result.json < data/val.txt

(saves to darknet/result.json)
'''

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
