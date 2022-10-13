import json
import requests


def main():
    data = {
        'username': 'james',
        'active': True,
        'subscribers': 10,
        'order_total': 39.99,
        'order_ids': ['ABC123', 'QQQ422', 'LOL300'],
    }
    print(data)
    # from python object to json string
    json_s = json.dumps(data)
    print(json_s)

    data_python = json.loads(json_s)
    print(data_python)

    # writing data to file
    with open('test_data.json', 'w') as f:
        json.dump(data, f)

    # reading data from file
    with open('test_data.json') as f:
        data3 = json.load(f)

    # Standard format in website (web APIs):
    # Example: free fake api
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    print(r.json())


if __name__ == '__main__':
    main()