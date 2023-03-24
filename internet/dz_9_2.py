import requests
import json


def get_info_dy_url(url):
    response = requests.get(url)
    print(response.headers)
    headers = dict(response.headers)
    return headers


def save_data_in_json(file_name, data):
    with open(file_name + ".json", "w") as out_file:
        json.dump(data, out_file, indent=4, sort_keys=True)


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/comments"
    data = get_info_dy_url(url)
    print(type(data))
    file = "data"
    # save_data_in_json(file, data)



