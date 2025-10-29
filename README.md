# 🐳 Docker Learning

This repository showcases several key projects built with Docker, tracking progress from initial attempts to completed setups.

---

### 🧩 hello_flask
A Flask application integrated with MySQL, fully containerized using Docker.  
This project follows through with the **CoderCo challenge** and serves as an initial learning exercise.

---

### 🚀 CoderCo Containers Challenge

#### flask_app1
- The **initial version** of the project.  
- Partially completed; lacked persistent storage, environment variables, and scaling/load balancing.  

#### flask_app2
- The **completed version** of the project.  
- Features **persistent Redis storage**, **environment variables**, and **scaling with multiple Flask instances** load-balanced via Docker Compose.  

---

### Features Implemented in flask_app2:
- **Flask Web Application**
  - `/` : Displays a homepage message.
  - `/count` : Increments and displays a visit count stored in Redis.
- **Redis Integration**
  - Connected Flask app to Redis using Python `redis` library.
  - Visit count is persisted in Redis using a Docker volume.
- **Application Scaling**
  - Multiple Flask instances run simultaneously.
  - Load balancing between instances handled via Docker Compose.

---

### 🚧 Features To Be Added / Learning Goals
- **Further Docker Optimization**
  - Nginx integration (reverse proxy) if required.
  - More advanced Docker Compose configurations.
