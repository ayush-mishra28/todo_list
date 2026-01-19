import requests

while True:
    task = input("Enter new task (Q to quit): ")

    if task.strip().lower() == "q":
        break

    requests.post(
        "http://localhost:5000/tasks",
        json={"title": task}
    )

    print("Task added\n")
