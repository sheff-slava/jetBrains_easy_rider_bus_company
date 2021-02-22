import json
import re

json_obj = '''[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]'''



python_obj = json.loads(input())
# python_obj = json.loads(json_obj)

# if python_obj != json.loads(json_obj):
#     print(json.dumps(python_obj, indent=4))

# stop_dict = dict()
bus_id_err = 0
stop_id_err = 0
stop_name_err = 0
next_stop_err = 0
stop_type_err = 0
a_time_err = 0

stop_name_template = '([A-Z][a-z]* )+(Road|Avenue|Boulevard|Street)$'
stop_type_template = '[SOF]?$'
date_template = '([0-1][0-9]|2[0-3]):[0-5][0-9]$'

line_128 = 0
line_256 = 0
line_512 = 0

for dict_ in python_obj:
    if dict_['bus_id'] == 128:
        line_128 += 1
    elif dict_['bus_id'] == 256:
        line_256 += 1
    elif dict_['bus_id'] == 512:
        line_512 += 1
    # if type(dict_['bus_id']) != int:
    #     bus_id_err += 1
    # if type(dict_['stop_id']) != int:
    #     stop_id_err += 1
    # if not re.match(stop_name_template, dict_['stop_name']):
    #     stop_name_err += 1
    # if type(dict_['next_stop']) != int:
    #     next_stop_err += 1
    # if not re.match(stop_type_template, dict_['stop_type']):
    #     stop_type_err += 1
    # if not re.match(date_template, dict_['a_time']):
    #     a_time_err += 1
    # if dict_['stop_name'] not in stop_dict.keys() and dict_['stop_name'] != '':
    #     stop_dict[dict_['stop_name']] = dict_['stop_id']
sum_ = bus_id_err + stop_id_err + stop_name_err + next_stop_err + stop_type_err + a_time_err

print('Line names and number of stops:',
      f'bus_id: 128, stops: {line_128}',
      f'bus_id: 256, stops: {line_256}',
      f'bus_id: 512, stops: {line_512}', sep='\n')

# print(f'Type and required field validation: {sum_} errors',
#       f'bus_id: {bus_id_err}', f'stop_id: {stop_id_err}',
#       f'stop_name: {stop_name_err}', f'next_stop: {next_stop_err}',
#       f'stop_type: {stop_type_err}', f'a_time: {a_time_err}', sep='\n')
