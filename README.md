# AI Resume Analyzer – CI/CD Pipeline Project

## 📌 Project Overview

The AI Resume Analyzer is a web-based application that allows users to upload their resume (PDF) and receive:

* Extracted skills
* Recommended job roles

This project demonstrates a **complete DevOps workflow**, including:

* CI/CD pipeline using Jenkins
* Automated testing (Unit + API + UI)
* Code quality checks
* Docker containerization
* Cloud deployment using Render

---

## 🌐 Live Deployment (Render)

🔗 https://devops-proj-resume-analyzer.onrender.com

The application is deployed on Render and accessible publicly.

---

## 🧱 Project Structure

project/
│
├── backend/
│   ├── app.py
│   └── uploads/
│
├── frontend/
│   └── index.html
│
├── tests/
│   ├── test_selenium.py
│   ├── test_app.py
│   └── sample.pdf
│
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md

---

## ⚙️ Technologies Used

* Python (Flask)
* HTML, CSS, JavaScript
* Selenium (UI Testing)
* Pytest (Unit & API Testing)
* Flake8 (Code Quality Analysis)
* Jenkins (CI/CD Pipeline)
* Docker (Containerization)
* GitHub (Version Control)
* Ngrok (Webhook exposure for Jenkins)
* Render (Cloud Deployment)

---

## 🚀 Features

* Upload resume in PDF format
* Extract skills using keyword-based analysis
* Recommend job roles dynamically
* Clean and responsive UI
* Automated testing (Unit + API + UI)
* Code quality checks using Flake8
* CI/CD automation with Jenkins
* Docker-based container deployment
* Live cloud deployment on Render

---

## 🔄 CI/CD Pipeline (Jenkins)

The Jenkins pipeline automates the entire workflow:

### 1️⃣ Clean Workspace

* Removes old files to avoid stale builds

### 2️⃣ Checkout Code

* Pulls latest code from GitHub repository

### 3️⃣ Install Dependencies

* Installs required Python packages

### 4️⃣ Start Backend Server

* Runs Flask backend for testing

### 5️⃣ Code Quality Check (Flake8)

* Performs static code analysis
* Non-blocking (pipeline continues even if issues found)

### 6️⃣ Run Unit & API Tests (Pytest)

* Executes backend tests
* Non-blocking to ensure pipeline continuity

### 7️⃣ Run Selenium Tests

* Tests UI functionality:

  * File upload
  * Button click
  * Result display

### 8️⃣ Stop Old Containers

* Stops any previously running Docker containers

### 9️⃣ Build Docker Image

* Builds application image

### 🔟 Run Docker Container

* Deploys application locally using Docker

---

## 🧪 Testing Strategy

### ✔ Unit Testing

* Tests core functions:

  * extract_skills()
  * recommend_jobs()

### ✔ API Testing

* Tests Flask endpoints:

  * POST /upload

### ✔ UI Testing (Selenium)

* Automates browser actions:

  * Upload resume
  * Click analyze button
  * Validate output

---

## 🔗 GitHub Webhook Integration

* GitHub webhook triggers Jenkins pipeline automatically on each push
* Ngrok is used to expose local Jenkins server

---

## ☁️ Deployment (Render)

* Application is deployed on Render
* Provides public access via URL
* Automatically runs backend service

---

## ▶️ How to Run Locally

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Run Backend

cd backend
python app.py

### 3. Open Application

http://127.0.0.1:5000

### 4. Run Tests

Unit & API tests:
pytest tests/test_app.py

Selenium tests:
python tests/test_selenium.py

---

## 🐳 Docker Usage

### Build Image

docker build -t ai-resume-analyzer .

### Run Container

docker run -d -p 5000:5000 ai-resume-analyzer

---

## ⚠️ Notes

* Ensure backend is running before Selenium tests
* Some tests are made non-blocking to avoid CI failures
* PyPDF2 may show deprecation warning but works correctly
* Jenkins workspace must be cleaned to avoid stale builds

---

## 🎯 Learning Outcomes

* End-to-end CI/CD pipeline implementation
* Integration of testing into DevOps workflow
* Static code analysis using Flake8
* Handling real-world CI/CD issues (webhooks, caching, environment differences)
* Docker-based deployment
* Cloud deployment using Render

---

## 🏁 Future Improvements

* Replace keyword-based logic with NLP/ML models
* Add database support
* Improve UI/UX
* Deploy using Kubernetes
* Add authentication system

---

## 📢 Conclusion

This project demonstrates a complete software development lifecycle integrating DevOps practices, automated testing, containerization, and cloud deployment, making it a comprehensive real-world application.

---
