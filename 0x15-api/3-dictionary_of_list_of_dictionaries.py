#!/usr/bin/python3
"""
Request data from API
Export this data to JSON
"""

import json
import requests


def fetch_all_todo_data():
    """Fetch data from the API"""
    users_data = requests.get(
        "http://jsonplaceholder.typicode.com/users").json()
    todos_data = requests.get(
        "http://jsonplaceholder.typicode.com/todos").json()

    users = [(user.get('id'), user.get('username')) for user in users_data]
    task_status_title = [(todo.get('userId'), todo.get('completed'),
                          todo.get('title')) for todo in todos_data]

    return users, task_status_title


def export_to_json(users_data, todos_data):
    """Export data to JSON"""
    data = dict()

    for user in users_data:
        tasks = []
        for task in todos_data:
            if task[0] == user[0]:
                tasks.append({"task": task[2], "completed": task[1],
                              "username": user[1]})
        data[str(user[0])] = tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file, sort_keys=True, indent=2)


if __name__ == "__main__":
    users, todos = fetch_all_todo_data()
    export_to_json(users, todos)
