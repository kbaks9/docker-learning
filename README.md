# 🐳 Docker Learning

This repository showcases two key projects built with Docker:

### 🧩 hello_flask
A Flask application integrated with MySQL, fully containerized using Docker.

### 🚀 CoderCo Containers Challenge
A multi-service setup featuring Flask and Redis.

### Features Implemented:
- **Flask Web Application**
  - `/` : Displays a welcome message.
  - `/count` : Increments and displays a visit count stored in Redis.
- **Redis Integration**
  - Connected Flask app to Redis using Python `redis` library.
  - Visit count is stored in Redis under the key `"visits"`.

---

### 🚧 Features To Be Added
- **Persistent Storage for Redis**  
  Configure Redis to use a volume to persist its data.
- **Environment Variables**  
  Modify the Flask application to read Redis connection details from environment variables and update the `docker-compose.yml` accordingly.
- **Scaling the Application**  
  Scale the Flask service to run multiple instances and load balance between them using Docker Compose.
