import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    data = [line.split(",") for line in data]
    dictionary = [{} for _ in range(1, len(data))]
    for value_index in range(1, len(dictionary)+1):
        for column_index in range(len(data[0])):
            dictionary[value_index-1].update({data[0][column_index]: data[value_index][column_index]})
    return dictionary


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
