# 🏦 ReFresh Bank  

**ReFresh Bank** is a comprehensive banking management system built with Django. It provides a seamless, secure, and user-friendly platform for both users and administrators to manage bank accounts, perform transactions, apply for loans, and more.  

---

## 🌟 Key Features  

### User Features  

- 🔑 **Secure Login & Registration:** Hassle-free account creation with top-notch security.  
- 💼 **Profile Management:** Update personal details, view transaction history, and manage accounts effortlessly.  
- 🔄 **Password Recovery & OTP Verification:** Enhanced account security with OTP-based authentication.  
- 💰 **Money Management:**  
  - Instantly deposit funds with email confirmations.  
  - Withdraw money securely with balance checks.  
  - Send money to other users using account numbers.  
- 📝 **Loan Applications:** Apply for loans with detailed terms and repayment options.  
- 📊 **Transaction Reports:** Access a detailed transaction history or filter reports by date range.  
- 📧 **Email Notifications:** Get instant updates for account activities, including deposits, withdrawals, transfers, and loan approvals.  

### Admin Features  

- 🏦 **Loan Management:** Review, approve, or reject loan applications seamlessly.  
- 🔍 **User Oversight:** Monitor and manage user accounts and transactions.  
- 🎛️ **Admin Dashboard:** Centralized control for streamlined management of key operations.  

---

## 🛠️ Technologies Used  

- **Backend:** `Python`, `Django Framework`, `Django REST Framework`  
- **Frontend:** `Django Templates`, `TailwindCSS` for responsive UI/UX  
- **Database:** `PostgreSQL` for reliable and secure data storage  
- **Utilities:** Integrated email notifications, Python logic for transaction ID generation  
 
---

## 📸 Screenshots  

Here are some key pages of the application:  

| **Home Page**               | **User Dashboard**             | **Admin Dashboard**             |
|------------------------------|---------------------------------|----------------------------------|
| ![Home Page](https://github.com/anmamun0/refresh-bank-webapp/blob/main/project_photos/un_authenticated_home-page.png) | ![User Dashboard](https://github.com/anmamun0/refresh-bank-webapp/blob/main/project_photos/authenticated_home-page.png) | ![Admin Dashboard](https://github.com/anmamun0/refresh-bank-webapp/blob/main/project_photos/transactions-report-page.png) |
 

---
 
## 📸 Screenshots  

### Home Page  
![Home Page](https://github.com/anmamun0/refresh-bank-webapp/project_photos/un_authenticated_home-page.png)

### User Dashboard  
![User Dashboard](https://github.com/anmamun0/refresh-bank-webapp/project_photos/authenticated_home-page.png)

### Admin Dashboard  
![Admin Dashboard](https://github.com/anmamun0/refresh-bank-webapp/project_photos/transactions-report-page.png)




---



## 📂 Project Structure  

```plaintext
├── manage.py                # Django project entry point  
├── app/                     # Main application directory  
│   ├── models.py            # Database models  
│   ├── views.py             # Business logic and controllers  
│   ├── urls.py              # URL routing  
│   ├── templates/           # HTML templates for UI  
│   └── static/              # Static files (CSS, JS, images)  
├── settings.py              # Project settings and configurations  
└── requirements.txt         # Python dependencies  
