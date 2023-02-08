#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.
Requirements:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(employeeId)).json()
    todos = requests.get(url + "todos", params={"userId": employeeId}).json()
    username = employee.get("username", "")

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                [employeeId, username, t.get("completed"), t.get("title")])
