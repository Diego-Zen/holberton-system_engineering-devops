#!/usr/bin/python3
"""
    Gather data from an API
"""
import json
import requests
import sys

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    r = requests.get('{}'.format(url_users))

    json_data = r.json()
    records = {}

    for user in json_data:
        user_id = user.get('id')
        name = user.get('username')
        r2 = requests.get(url_todos, params={'userId': user_id})
        json_data_r2 = r2.json()

        tasks = []

        for task in json_data_r2:
            my_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name
            }
            tasks.append(my_dict)

            records[str(user_id)] = tasks

    filename = "todo_all_employees.json"
    with open(filename, mode="w") as f:
        json.dump(records, f)
