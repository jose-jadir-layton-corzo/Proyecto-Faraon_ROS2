# 🏺 Proyecto Faraón: Industrial IoT & ROS 2 on Legacy Hardware

This project demonstrates the implementation of a **Sistemas de Sistemas (SoS)** architecture using ROS 2 Humble and Docker on a 2008 PC (2.6 GB RAM).

## 🚀 Engineering Milestones
*   **Resource Optimization:** Successfully deployed ROS 2 Humble on legacy hardware with critical memory constraints.
*   **Asynchronous Control:** Implemented a Multithreaded Python Server (`ThreadingMixIn`) to handle real-time MJPEG video and serial commands simultaneously.
*   **Global Connectivity:** Secure HTTPS tunneling via **Ngrok** with an asynchronous Fetch API frontend to eliminate UI latency.
*   **Power Electronics:** Direct AC power control via Arduino Mini + TRIAC/MOC stage.

## 🛠️ Tech Stack
*   **Middleware:** ROS 2 Humble (Dockerized).
*   **Backend:** Python 3 (Threading, Serial, HTTP).
*   **Hardware:** Arduino Mini, Webcam Cubeternet, PC 2008 (Debian 12).
*   **Networking:** WebSockets, Ngrok, Fetch API.

## 📈 Future Roadmap
*   Integration of **Zenoh** for ultra-low latency interoperability.
*   Hardware-in-the-Loop (HIL) simulation for industrial fleet orchestration.

---
*Developed by Jose Jadir Layton Corzo - 2026*
