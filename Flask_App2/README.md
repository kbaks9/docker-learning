# Flask + Redis Web App

This project is a simple **Flask** web application backed by **Redis** for visitor tracking.  
It’s part of my ongoing learning series in Dockerized web application deployment.

---

## 🧱 Project Overview

The app exposes two endpoints:

- **`/`** — Homepage with a link to the visitor count page.  
- **`/count`** — Displays the number of visitors, tracked persistently via Redis.

---

## 🆕 Updates Since the Previous (Deprecated) Version

From the last iteration of this project, I’ve made the following improvements:

- ✅ **Added persistent storage** for Redis data to ensure counts are retained even after container restarts.  
- ✅ **Introduced environment variables** for configurable parameters such as host, port, and Redis connection details.

---

## 🚀 Next Steps (Final Phase)

Tomorrow’s final iteration will include:

- 🔹 **Nginx integration** for serving the Flask app as a reverse proxy.  
- 🔹 **Load balancing setup** to handle multiple Flask containers efficiently.

---

## 🧩 Tech Stack

- **Flask** (Python)
- **Redis**
- **Docker**
- **Docker Compose**
- *(Upcoming)* **Nginx**

---

## 🖥️ Run the Application

```bash
docker-compose up --build