#!/usr/bin/python3
"""
    Gather data from an API
"""
import json
import requests
import sys

if __name__ == "__main__":
    search = sys.argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    r = requests.get('{}{}'.format(url_users, search))
    r2 = requests.get(url_todos, params={'userId': search})

    json_data = r.json()
    json_data_r2 = r2.json()

    tasks = []

    for task in json_data_r2:
        my_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": json_data.get('username')
        }
        tasks.append(my_dict)

    records = {str(search): tasks}
    filename = "{}.json".format(search)
    with open(filename, mode="w") as f:
        json.dump(records, f)
