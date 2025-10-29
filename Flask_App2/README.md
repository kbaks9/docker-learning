# 🚀 Flask + Redis Web App (Final Version)

This project is a containerized **Flask + Redis** web application deployed with **Docker Compose**, now featuring **application scaling and load balancing** for improved performance and reliability.

---

## 🧱 Project Overview

The application includes:

- 🐍 **Flask (Python)** — Handles the web logic and visitor counter.  
- 🧠 **Redis** — Stores persistent visitor counts across containers.  
- ⚖️ **Scaled Flask instances** — The app runs multiple Flask containers, with **load balancing handled automatically through Docker Compose**.

### 🔗 Endpoints
- **`/`** — Homepage with a link to the visitor count page.  
- **`/count`** — Displays the total number of visitors tracked by Redis.

---

## 🔄 Updates & Improvements

Since the deprecated version, the project has evolved significantly:

- 💾 Added **persistent storage** using Docker volumes for Redis data retention.  
- ⚙️ Introduced **environment variables** for flexible configuration.  
- ⚖️ **Scaled the Flask application** to run multiple instances and **load balance traffic** between them using Docker Compose.

---

## 🏗️ Architecture Overview

Client requests are distributed evenly across multiple **Flask containers**, each connected to the same **Redis** data store.  
This ensures consistent visitor counts and improved availability when scaling horizontally.

---

## 🧩 Tech Stack

- 🐍 Flask (Python)  
- 🧠 Redis  
- 🐳 Docker  
- 🧭 Docker Compose  

---

## 💻 How to Run

```bash
# 1. Build and start all containers
docker compose up --build

# 2. Access the app
# Visit http://localhost
# Endpoints:
#   /     — Homepage
#   /count — Visitor count page

# 3. Optional: Scale Flask app to multiple instances
docker compose up --scale web=3
