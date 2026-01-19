import requests

task_id = int(input("Enter task ID to delete: "))

requests.delete(f"http://localhost:5000/tasks/{task_id}")

print("Task deleted")
