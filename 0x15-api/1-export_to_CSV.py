#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]
    user = requests.get(url + "users/{}".format(userId)).json().get('username')
    todo = requests.get(url + "todos", params={"userId": userId}).json()
    taskList = []

    fileName = "{}.csv".format(userId)
    with open(fileName, 'w', newline='') as cFile:
        writer = csv.writer(cFile, quoting=csv.QUOTE_ALL)
        for item in todo:
            taskList.append([userId, user, item.get('completed'),
                             item.get('title')])

        writer.writerows(taskList)
