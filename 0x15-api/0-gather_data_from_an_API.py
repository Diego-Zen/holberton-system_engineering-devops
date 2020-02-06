#!/usr/bin/python3
"""
    Gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    search = sys.argv[1]
    done = 0
    total = 0
    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(search)
    )
    r2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos/',
        params={'userId': search}
    )
    json_data = r.json()
    json_data_r2 = r2.json()
    for task in json_data_r2:
        total = total + 1
        if task.get('completed') is True:
            done = done + 1

    print(
        "Employee {} is done with tasks({}/{})"
        .format(
            json_data.get('name'),
            done, total
        )
    )

    for task in json_data_r2:
        if task.get('completed') is True:
            print("\t{}".format(task.get('title')))
