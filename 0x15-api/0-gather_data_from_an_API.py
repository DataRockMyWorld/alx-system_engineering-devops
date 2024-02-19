#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done_tasks = [task for task in tasks if task.get('completed')]
    done = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks ({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t{task.get('title')}")
