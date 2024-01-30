#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import requests
from sys import argv


if __name__ == "__main__":

     url = "https://jsonplaceholder.typicode.com/"
     user = requests.get(url + "users/{}".format(argv[1])).json().get('name')
     todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
     todoList = []
     for item in todo:
          if item.get('completed') is True:
               todoList.append(item.get('title'))
     print("Employee {} is done with tasks({}/{}):".format(
          user, len(todoList), len(todo)))
     [print("\t {}".format(item)) for item in todoList]
