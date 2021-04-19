import json


def check_time(time_1, time_2):
    h_1, m_1 = time_1.split(':')
    h_2, m_2 = time_2.split(':')
    h_1 = int(h_1[1]) if h_1.startswith('0') else int(h_1)
    h_2 = int(h_2[1]) if h_2.startswith('0') else int(h_2)
    m_1 = int(m_1[1]) if m_1.startswith('0') else int(m_1)
    m_2 = int(m_2[1]) if m_2.startswith('0') else int(m_2)
    if h_1 < h_2:
        return True
    elif h_1 > h_2:
        return False
    else:
        if m_1 < m_2:
            return True
        elif m_1 >= m_2:
            return False


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
        "a_time": "08:17"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:07"
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
        "a_time": "09:44"
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

json_obj2 = '''[
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


list_of_dict = json.loads(input())
# list_of_dict = json.loads(json_obj1)
# list_of_dict.sort(key=lambda x: x['bus_id'])

wrong_time_dict = dict()
bus_id = list_of_dict[0]['bus_id']
found_wrong_time = False
i = 0
for i in range(len(list_of_dict) - 1):
    if not found_wrong_time and not check_time(list_of_dict[i]['a_time'], list_of_dict[i + 1]['a_time'])\
            and list_of_dict[i]['bus_id'] == list_of_dict[i + 1]['bus_id']:
        wrong_time_dict[bus_id] = list_of_dict[i + 1]['stop_name']
        found_wrong_time = True
    elif list_of_dict[i]['bus_id'] != list_of_dict[i + 1]['bus_id']:
        bus_id = list_of_dict[i + 1]['bus_id']
        found_wrong_time = False

print('Arrival time test:')
if len(wrong_time_dict) == 0:
    print('OK')
else:
    for line, station in wrong_time_dict.items():
        print(f'bus_id line {line}: wrong time on station {station}')
