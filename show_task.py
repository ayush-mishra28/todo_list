import requests

response = requests.get("http://localhost:5000/tasks")
tasks = response.json()

print("--------- TO_DO_LIST ---------")
if not tasks:
    print("No tasks found.")
else:
    for t in tasks:
        status = "✔" if t["done"] else "✗"
        print(f"{t['id']}. {t['title']} [{status}]")
print("------------------------------")
