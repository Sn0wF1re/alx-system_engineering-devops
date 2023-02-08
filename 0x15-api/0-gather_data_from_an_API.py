#!/usr/bin/python3
"""
Uses REST API, given employee ID to return info about their TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employeeId = sys.argv[1]
    employee = requests.get(f'{url}users/{employeeId}').json()
    todos = requests.get(f'{url}todos', params={'userId': employeeId}).json()

    completed = [t.get('title') for t in todos if t.get('completed', False)]

    output = "Employee {EMPLOYEE_NAME} is done " \
             "with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    print(output.format(
        EMPLOYEE_NAME=employee.get("name"),
        NUMBER_OF_DONE_TASKS=len(completed),
        TOTAL_NUMBER_OF_TASKS=len(todos)))
    for x in completed:
        print(f'\t {x}')
