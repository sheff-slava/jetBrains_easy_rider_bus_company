import json


json_obj1 = '''[
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
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "",
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

json_obj2 = '''[
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


list_of_dict = list(json.loads(input()))
# list_of_dict = list(json.loads(json_obj2))
list_of_dict.sort(key=lambda x: x['bus_id'])

start_set = set()
finish_set = set()
stops_by_lines = dict()

bus_id = list_of_dict[0]['bus_id']
start_count = 0
finish_count = 0
no_start_finish = False
i = 0
while i < len(list_of_dict):
    while list_of_dict[i]['bus_id'] == bus_id:
        if list_of_dict[i]['stop_type'] == 'S':
            start_count += 1
            start_set.update({list_of_dict[i]['stop_name']})
        elif list_of_dict[i]['stop_type'] == 'F':
            finish_count += 1
            finish_set.update({list_of_dict[i]['stop_name']})
        if list_of_dict[i]['stop_name'] not in stops_by_lines.keys():
            list_ = list()
            list_.append(bus_id)
            stops_by_lines[list_of_dict[i]['stop_name']] = list_
        else:
            list_ = stops_by_lines[list_of_dict[i]['stop_name']]
            list_.append(bus_id)
            stops_by_lines[list_of_dict[i]['stop_name']] = list_
        i += 1
        if i == len(list_of_dict):
            break
    if start_count != 1 or finish_count != 1:
        print(f'There is no start or end stop for the line: {bus_id}.')
        no_start_finish = True
        break
    elif i < len(list_of_dict):
        bus_id = list_of_dict[i]['bus_id']
        start_count = 0
        finish_count = 0

if not no_start_finish:
    start_stops = list(start_set)
    transfer_stops = list()
    finish_stops = list(finish_set)
    for stop, list_id in stops_by_lines.items():
        if len(list_id) > 1:
            transfer_stops.append(stop)
    print('Start stops:', len(start_stops), sorted(start_stops))
    print('Transfer stops:', len(transfer_stops), sorted(transfer_stops))
    print('Finish stops:', len(finish_stops), sorted(finish_stops))
