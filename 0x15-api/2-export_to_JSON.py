#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
Requirements:
Records all tasks that are owned by this employee
Format must be: { "USER_ID":
[{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employeeId)).json()
    todos = requests.get(url + "todos", params={"userId": employeeId}).json()
    username = employee.get("username", "")

    with open("{}.json".format(employeeId), "w") as jsonfile:
        json.dump({"{employeeId}".format(employeeId=employeeId): [{
            "task": t.get("title"), "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
