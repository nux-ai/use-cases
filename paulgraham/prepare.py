import requests
import json


def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def send_payload(payload_data):
    url = "http://localhost:7789/v1/source/create"

    headers = {
        'Authorization': 'sk_nw4MHC0RIiDiqHWHhK2SKT4gnzs5iAUX-ALVQPq-y5rCWteDDCk14lYskdOrh5HwpcU',
        'Content-Type': 'application/json'
    }

    payload = json.dumps(payload_data)

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if __name__ == "__main__":
    # Read the JSON file into a variable
    payload_data = read_json_file('pg_essays.json')

    # Send the data
    send_payload(payload_data)
