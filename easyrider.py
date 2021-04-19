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
        "stop_type": "O",
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
        "stop_type": "O",
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
# list_of_dict = json.loads(json_obj2)
# list_of_dict.sort(key=lambda x: x['bus_id'])

wrong_stops_list = list()
for dict_ in list_of_dict:
    if dict_['stop_type'] == 'O' and dict_['stop_name'] != 'Fifth Avenue':
        wrong_stops_list.append(dict_['stop_name'])

print('On demand stops test:')
if len(wrong_stops_list) == 0:
    print('OK')
else:
    wrong_stops_list.sort()
    print('Wrong stop type:', wrong_stops_list)
