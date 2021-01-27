import json

file_name='csvjson'
pk = 0
new_list = []
c = -1
with open('{}.json'.format(file_name)) as json_data:
    d = json.load(json_data)    
    for item in d:
        c+=1
        if(c==50000): break
        pk+=1
        item = {"model": "api.BankDetail", "pk": pk, "fields": item}
        new_list.append(item)
        json_data.close()


def list_to_json_file(list_of_dicts, file_name):
    with open(file_name+'.json', 'w') as file:
        json.dump(list_of_dicts, file)
    print('{}.Json file created'.format(file_name))


list_to_json_file(new_list, 'data_fixtures_s')
