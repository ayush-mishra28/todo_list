import requests


response = requests.get("http://localhost:5000/tasks")
tasks = response.json()

print("--------- TO_DO_LIST ---------")
if not tasks:
    print("No tasks available.")
    exit()

for t in tasks:
    status = "✔" if t["done"] else "✗"
    print(f"{t['id']}. {t['title']} [{status}]")
print("------------------------------")


task_id = input("Enter task ID to mark complete (Q to quit): ")

if task_id.strip().lower() == "q":
    exit()


requests.put(f"http://localhost:5000/tasks/{int(task_id)}")

print("Task marked complete")
