import os
from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "todo_app")
    )

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    return jsonify([
        {"id": t[0], "title": t[1], "done": bool(t[2])}
        for t in tasks
    ])

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)",
        (data["title"],)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET done = TRUE WHERE id = %s",
        (task_id,)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task completed"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
