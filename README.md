# 💡 DevOps Wisdom: Microservices & GitOps Showcase

This project is a Senior-level DevOps demonstration featuring a polyglot microservices architecture, automated CI/CD pipelines, and local Kubernetes orchestration.

## 🏗️ Architecture
- **Backend:** High-performance API built with **Go (Gin Framework)**.
- **Frontend:** Responsive web interface built with **Python (Flask)**.
- **Containerization:** Multi-stage Docker builds for minimal security footprint (Alpine-based).
- **Orchestration:** **Kubernetes (K8s)** manifests with resource limits and high availability (2 replicas for backend).
- **CI/CD:** Automated pipeline via **GitHub Actions** with integrated security scanning.

## 🛠️ Tech Stack
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 🛡️ DevSecOps
Every push to `main` triggers an automated workflow that:
1. **Builds** Docker images for both services.
2. **Scans** images for vulnerabilities using **Trivy** (Targeting CRITICAL and HIGH severities).
3. **Publishes** secure images to **GitHub Container Registry (GHCR)**.

## 🚀 Local Setup (Kubernetes)
To run this project on your local machine using **Kind**:

1. **Create Cluster:**
   ```bash
   kind create cluster --name wisdom-cluster

2. **Apply Manifests**
    ```bash
    kubectl apply -f k8s/

3. **Access App:**
    ```bash
    kubectl port-forward service/frontend-service 8080:80
    
    Open http://localhost:8080 in your browser.