#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(url + "users/{}".format(userId)).json().get('username')
    todo = requests.get(url + "todos", params={"userId": userId}).json()
    taskList = []

    fileName = "{}.json".format(userId)
    with open(fileName, 'w', newline='') as jFile:
        json.dump({userId: [{"task": line.get("title"),
                             "completed": line.get("completed"),
                             "username": user} for line in todo]}, jFile)
