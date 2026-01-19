# To-Do Application (Python + MySQL + API)

This project demonstrates a CRUD-based To-Do application using:
- Python
- Flask REST API
- MySQL database

## Architecture
Client Scripts → Flask API → MySQL Database

## Features
- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks

## Setup Instructions

1. Install MySQL and create database:
   ```bash
   mysql -u root -p < schema.sql
   ```
2. Create .env file (use .env.example as reference)

3. Install dependencies:

- pip install -r requirements.txt


4. Start API:
   ```bash
   python api.py
   ```

5. Run client scripts:
   ```bash
   python add_task.py
   python show_tasks.py
   ```

## NOTES
- Database credentials are handled using environment variables


- .env is intentionally excluded from version control