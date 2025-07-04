# 🧮 Cloud-Based Calculator Application

This is a simple calculator web application with persistent history functionality, deployed on AWS using a secure two-tier architecture. The frontend is built using HTML, CSS, and JavaScript, while the backend is powered by Django (Python). The application is deployed across two EC2 instances within a custom VPC using proper public/private subnet segregation.

## 🚀 Features

- Perform basic arithmetic operations (+, -, ×, ÷)
- Stores each calculation in a CSV file on the backend
- Displays full calculation history on page load
- Secure AWS deployment using a private/public subnet structure

---

## 🛠️ Tech Stack

**Frontend:**
- HTML, CSS, JavaScript
- Hosted on EC2 (Public Subnet)

**Backend:**
- Python, Django
- Hosted on EC2 (Private Subnet)
- Stores calculation history in a local CSV file (`history.csv`)

**Cloud Infrastructure:**
- Amazon EC2 (2 instances: frontend & backend)
- Amazon VPC with:
  - 1 Public Subnet (frontend)
  - 1 Private Subnet (backend)
- Internet Gateway for outbound internet access
- NAT Gateway to allow backend access to the internet
- Custom route tables and security groups

---

## ⚙️ How It Works

1. **User Interface**  
   User interacts with the frontend (calculator UI), performs operations, and hits "=".

2. **API Call to Backend**  
   JavaScript sends a `POST` request to the Django backend with the expression (e.g., `2+3`).

3. **Server-Side Evaluation**  
   The Django server evaluates the expression, stores the result in a `history.csv` file with a timestamp, and returns the result.

4. **Display Results & History**  
   On page load, the frontend sends a `GET` request to fetch calculation history from the backend and displays it on the UI.

---

## 🗂️ Project Structure

