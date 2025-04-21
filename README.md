# 🚀 Flask Task Management API - DevOps Edition

A **Flask-based RESTful API** for task management, enhanced with full **CI/CD**, **Docker Swarm**, and **GitHub Actions** for seamless deployment and scalability.

---

## 📋 Features

- 🔧 Create, Read, Update, Delete (CRUD) Tasks
- ✅ Task status with enum validation (`pending`, `in-progress`, `completed`)
- 🔁 Stateless, in-memory data store (great for demos/POCs)
- 🐳 Dockerized for containerized environments
- ☸️ Docker Swarm support for scalability and HA
- ⚙️ CI/CD via GitHub Actions

---

## 🧠 API Overview

### 🔧 Base URL
http://localhost:5000/


### 📦 Endpoints

| Method | Endpoint       | Description           |
|--------|----------------|-----------------------|
| GET    | `/tasks`       | List all tasks        |
| POST   | `/tasks`       | Create a new task     |
| GET    | `/tasks/<id>`  | Retrieve task by ID   |
| PUT    | `/tasks/<id>`  | Update task by ID     |
| DELETE | `/tasks/<id>`  | Delete task by ID     |

---

## 🧱 Sample Task Payload

```json
{
  "title": "Build CI/CD pipeline",
  "description": "Use GitHub Actions for Docker build and deploy",
  "status": "in-progress"
}
