import json


json_obj = '''[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
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
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
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
        "next_stop": "0",
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
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]'''

python_obj = json.loads(input())
# python_obj = json.loads(json_obj)

stop_dict = dict()
bus_id_err = 0
stop_id_err = 0
stop_name_err = 0
next_stop_err = 0
stop_type_err = 0
a_time_err = 0

for dict_ in python_obj:
    if type(dict_['bus_id']) != int:
        bus_id_err += 1
    if type(dict_['stop_id']) != int:
        stop_id_err += 1
    if type(dict_['stop_name']) != str or dict_['stop_name'] == '':
        stop_name_err += 1
    if type(dict_['next_stop']) != int:
        next_stop_err += 1
    if dict_['stop_type'] not in ('', 'S', 'O', 'F'):
        stop_type_err += 1
    if type(dict_['a_time']) != str or dict_['a_time'] == '':
        a_time_err += 1
    if dict_['stop_name'] not in stop_dict.keys() and dict_['stop_name'] != '':
        stop_dict[dict_['stop_name']] = dict_['stop_id']
sum_ = bus_id_err + stop_id_err + stop_name_err + next_stop_err + stop_type_err + a_time_err
print(f'Type and required field validation: {sum_} errors',
      f'bus_id: {bus_id_err}', f'stop_id: {stop_id_err}',
      f'stop_name: {stop_name_err}', f'next_stop: {next_stop_err}',
      f'stop_type: {stop_type_err}', f'a_time: {a_time_err}', sep='\n')
